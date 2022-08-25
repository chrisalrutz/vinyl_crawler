# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Listing(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    labelCat = scrapy.Field()
    itemCatNo = scrapy.Field()
    sleeveCondition = scrapy.Field()
    rUrl = scrapy.Field()
    price = scrapy.Field()

    pass
