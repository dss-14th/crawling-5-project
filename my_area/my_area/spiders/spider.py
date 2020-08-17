import scrapy
from my_area.items import My_areaItem

class AreaSpider(scrapy.Spider):
    name = "MyArea"
    allow_domain = ["https://m.naver.com"]
    start_urls = ["https://m.naver.com/history/?menu=PLACE_09"]
    
    def parse(self, response):
        links = response.xpath('//*[@id="mflick"]/div/div[2]/div/div[1]/div[1]')[0].xpath('//*[@class="cvr_list_item"]/a/@href').extract()
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.parse_contents)
                        
    def parse_content(self, response):
        item = My_areaItem()
        item["title"] = response.xpath('//*[@id="SE-34941879-7272-46c4-b494-066d46aaec3b"]/text()').extract()[0]
        item["day"] = response.xpath('//*[@id="SE-0bcb5c34-10d6-46a2-976d-0437c9a0bf58"]/div/div/div[3]/p/text()').extract()[0].strip()
        item["comment"] = response.xpath('//*[@id="ct"]/div[4]/div[3]/div/div[2]/a[1]/em/text()').extract()[0]
        item["link"] = response.url
        yield item
