import scrapy

class MeetupItem(scrapy.Item):

	url = scrapy.Field()
	name = scrapy.Field()
	city = scrapy.Field()
	country = scrapy.Field()
	founded = scrapy.Field()
	
	description = scrapy.Field()
	members = scrapy.Field()
	meetups = scrapy.Field()
	topics = scrapy.Field()
