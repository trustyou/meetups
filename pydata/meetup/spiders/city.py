import logging
import re
import urllib

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from meetup.items import MeetupItem

def first_or_none(xs):
	try:
		return xs[0]
	except IndexError:
		return None

class ParseMeetupMixin:
	def parse_meetup(self, response):
		m = MeetupItem()

		org_div = response.selector.css("div[itemtype='http://schema.org/Organization']")
		if not len(org_div) == 1:
			# we're not on a meetup page
			return

		m["url"] =  first_or_none(org_div.css("[itemprop=url]::text").extract())
		m["name"] = first_or_none(org_div.css("[itemprop=name]::text").extract())
		m["city"] = first_or_none(org_div.css("[itemprop=addressLocality]::text").extract())
		m["country"] = first_or_none(response.selector.css("meta[property='og:country-name']").xpath("@content").extract())
		m["founded"] = first_or_none(org_div.css("[itemprop=foundingDate]::text").extract())

		m["description"] = "".join(response.selector.css(".groupDesc ::text").extract()).strip()
		m["topics"] = response.selector.css("[id^=topicList] a::text").extract()
		m["members"] = (response.selector.css("a[href$='/members/']>.lastUnit").re(r"\d+") or [None])[0]
		m["meetups"] = (response.selector.css("a[href*='/events/past/']>.lastUnit").re(r"\d+") or [None])[0]

		yield m

class CitySpider(CrawlSpider, ParseMeetupMixin):

	name = "city"
	allowed_domains = ["www.meetup.com"]
	rules = [
		Rule(LinkExtractor(allow=[
			r"^http://www.meetup.com/find/\?",
		]), callback='parse_find'),
		Rule(LinkExtractor(allow=[
			'^http://www.meetup.com/[^/]+/$',
		]), callback='parse_meetup'),
	]

	def __init__(self, city="", *args, **kwargs):
		super(CitySpider, self).__init__(*args, **kwargs)

		self.start_urls = [
			"http://www.meetup.com/find/?allMeetups=true&radius=50&userFreeform={}".format(city)
		]

	def parse_find(self, response):

		meetups = response.selector.css(".groupCard")
		if not meetups:
			# Meetup.com returns an empty page if the pageToken exceeds the
			# number of meetups in the city. Exploit this behavior to stop
			# paging before we go on indefinitely ...
			logging.info("Stopped paging after {}".format(response.url))
			return
		
		page_token = response.selector.css("#simple-data").xpath("@data-pagetoken").extract()[0]
		next_url = re.sub("&pageToken=[^&]+", "", response.url) + "&" + urllib.urlencode({"pageToken": page_token})

		yield Request(
			next_url,
			# scrapy considers this a duplicate request - override this decision:
			dont_filter=True
		)

