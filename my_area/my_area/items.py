
import scrapy

class My_areaItem(scrapy.Item):
    title = scrapy.Field()
    good = scrapy.Field()
    comment = scrapy.Field()
    day = scrapy.Field()
    link = scrapy.Field()    
