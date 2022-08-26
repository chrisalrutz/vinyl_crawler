import scrapy
from scrapy import Request

class SellersPySpider(scrapy.Spider):
    name = 'sellers.py'
    allowed_domains = ['discogs.com']

#https://www.discogs.com/sell/list?format=Vinyl&ships_from=United+States#more%3Dseller    

    def start_requests(self):
        urls = ['https://www.discogs.com/sell/list?format=Vinyl&ships_from=']
        countries = [
            'United+States',
            'United+Kingdom',
            'Germany',
            'Italy',
            'France',
            'Netherlands',
            'Spain',
            'Denmark',
            'Belgium',
            'Canada',
            'Japan',
            'Greece',
            'Sweden',
            'Portugal',
            'Austrailia',
            'Austria',
            'Switzerland',
            'Brazil',
            'Hungary',
            'Poland',
            'Lithuania',
            'Finland',
            'Czech+Republic',
            'China',
            'Norway',
            'Mexico',
            'Serbia',
            'Croatia',
            'Argentina',
            'Israel',
            'Neutral+Zone',
            'Venezuela',
            'Ireland',
            'Jamaica',
            'Ukraine',
            'Turkey',
            'Slovak Republic',
            'Colombia',
            'South+Africa',
            'Romania',
            'Peru',
            'Latvia',
            'Bulgaria',
            'New+Zealand',
            'Estonia',
            'Slovenia',
            'Northern+Ireland',
            'Macedonia',
            'South+Korea',
            'Belarus',
            'India',
            'Luxembourg',
            'Cyprus',
            'Hong+Kong',
            'Chile',
            'Malta',
            'Taiwan',
            'Indonesia',
            'Singapore',
            'Armenia',
            'Ecuador',
            'Andorra',
            'Morocco',
            'Malaysia',
            'Thailand',
            'Uruguay',
            'Iceland',
            'Lebanon',
            'Philippines',
            'Vietnam',
            'Georgia',
            'Aruba',
            'Kenya',
            'Costa+Rica',
            'San+Marino',
            'Panama',
            'El+Salvador',
            'Nigeria',
            'Uganda',
            'Uzbekistan',
            'Bolivia',
            'United+Arab+Emirates',
            'Monaco',
            'Bahrain',
            'Tunisia',
            'Puerto+Rico',
            'Macau',
            'Mongolia',
            'Montenegro',
            'Kyrgyzstan',
        ]

        for url in urls:
            for country in countries:
                urlnew = url +  + country + '#more%3Dseller'
                yield Request(url=urlnew, callback=self.parse)

    def parse(self, response):
        for seller in response.xpath('//article'):
            yield{
                'name' : response.xpath('//div[@class="rs-block md:rs-text-xl rs-font-bold"]/text()').get(),
                'location' : response.xpath('//div[@class="rs-mt-2 rs-text-sm md:rs-text-base"]/text()')[1].get(),
                'sUrl' : response.xpath('//article/a').attrib['href']
            }

# /div[1]/div[4]/div[3]/div[2]/div/ul/li[1]/ul/li[2]/a/span[2]
//*[@id="more_filters_container"]/ul/li[1]/ul/li[2]/a/span[2]

https://www.discogs.com/style/musique+concr%C3%A8te