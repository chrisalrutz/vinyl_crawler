import scrapy


class StylesSpider(scrapy.Spider):
    name = 'styles'
    allowed_domains = ['Users']
    start_urls = ['http://Users/']

    def parse(self, response):
        pass
