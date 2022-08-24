import scrapy


class RecordlistingsPySpider(scrapy.Spider):
    name = 'recordListings.py'
    allowed_domains = ['www.discogs.com']
    
    def start_requests(self):
        urls = ['https://www.discogs.com/seller/philadelphiamusic/profile?format=Vinyl&genre=Electronic',
                'https://www.discogs.com/seller/philadelphiamusic/profile?format=Vinyl&genre=Hip+Hop',
                'https://www.discogs.com/seller/philadelphiamusic/profile?format=Vinyl&genre=Jazz',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for listing in response.xpath('//tr[@class="shortcut_navigable "]'):
            title = response.xpath('//p[@class="item_description_title"]').get()
            labelCat = response.xpath('//p[@class="label_and_cat"]').getall()
            itemCatNo = response.xpath('//span[@class="label_and_cat"]').get()
            sleeveCondition = response.xpath('//span[@class="item_sleeve_condition"]').get()
            rUrl = response.xpath('//a[@class="item_release_link"]').get()
            price = response.xpath('//span[@class="price"]').get()

        next_page = response.xpath('//a[@class="pagination_next"]').attrib['href']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

