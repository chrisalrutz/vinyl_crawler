import scrapy
from discogs_crawler.items import Listing

class RecordlistingsPySpider(scrapy.Spider):
    name = 'recordListings.py'
    allowed_domains = ['www.discogs.com']
    listings = []

    def start_requests(self):
        urls = ['https://www.discogs.com/seller/philadelphiamusic/profile?format=Vinyl&genre=Electronic',
                'https://www.discogs.com/seller/philadelphiamusic/profile?format=Vinyl&genre=Hip+Hop',
                'https://www.discogs.com/seller/philadelphiamusic/profile?format=Vinyl&genre=Jazz',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        listings = []
        for listing in response.xpath('//tr[@class="shortcut_navigable "]'):
            yield{
                'title' : response.xpath('//a[@class="item_description_title"]/text()').get(),
                'label' : response.xpath('//p[@class="hide_mobile label_and_cat"]/a/text()').get(),
                'itemCatNo' : response.xpath('//p[@class="hide_mobile label_and_cat"]/span[@class="item_catno"]/text()').get(),
                'sleeveCondition' : response.xpath('//span[@class="item_sleeve_condition"]/text()').get(),
                'Url' : response.xpath('//a[@class="item_release_link hide_mobile"]').attrib['href'],
                'price' : response.xpath('//span[@class="price"]/text()').get()
            }

            # thisListing = Listing()
            # thisListing['title'] = title
            # thisListing['labelCat'] = labelCat
            # thisListing['itemCatNo'] = itemCatNo
            # thisListing['sleeveCondition'] = sleeveCondition
            # thisListing['rUrl'] = rUrl
            # thisListing['price'] = price
            # listings.append(thisListing)

        next_page = response.xpath('//a[@class="pagination_next"]').attrib['href']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

