
import scrapy

class My_areaItem(scrapy.Item):
    title = scrapy.Field()
    comment = scrapy.Field()
    day = scrapy.Field()
    link = scrapy.Field()
