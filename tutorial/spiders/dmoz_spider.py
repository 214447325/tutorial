import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        'http://image.baidu.com/'
    ]

    def parse(self, response):
        for sel in response.xpath('//div'):
            item = DmozItem()
            # item['title'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item