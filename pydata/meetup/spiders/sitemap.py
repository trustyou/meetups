from scrapy.spiders import SitemapSpider

from meetup.spiders.city import ParseMeetupMixin

class SitemapSpider(SitemapSpider, ParseMeetupMixin):
	
	name = "sitemap"

	sitemap_urls = [
		"http://www.meetup.com/sitemap.xml",
	]

	sitemap_rules = [
		(r"^http://www\.meetup.com/[^/]+/$", "parse_meetup"),
	]
