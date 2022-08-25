import scrapy
from vinyl_crawler.items import Listing

class RecordlistingsPySpider(scrapy.Spider):
    name = 'recordListings.py'
    allowed_domains = ['www.discogs.com']
    listings = []

    def start_requests(self):
        urls = [
                'https://www.discogs.com/seller/'
                ]
                
        genres = ['&genre=Electronic',
                  '&genre=Hip+Hop',
                  '&genre=Jazz',
                  '&genre=Folk%2C+World%2C+%26+Country',
                  '&genre=Classical',
                  '&genre=Stage+%26+Screen',
                  '&genre=Blues',
                  '&genre=Non-Music',
                  '&genre=Reggae',
                  '&genre=Children%27s',
                  '&genre=Brass+%26+Military'
                  '&genre=Funk+%2F+Soul',
                  '&genre=Pop',
                  '&genre=Rock',
                  ]

        sellers = ['Criminal-Rewind', 'ellaguru', 'Morpho_Chicago',
        'RoundTripRecords', 'ToneDeafRecords', 'Wild_Prairie', 
        'BucketOBlood', 'Meteor_Gem', 'lets_boogie_records', 'vvmo', 
        'Treasuregate', 'ShadyRest.Chicago', '606records', 'bluevillagevinyl', 
        'cheapkissrecords', 'TheConservatoryVinyl', 'thedenrecords', 'trustyspot', 
        'WeirdsvilleRecords', 'DetroitRecordClub', 'UHF-Records', 'streetcorner12', 
        'bradhales', 'dearbornm-farmington', 'RockCityMusicCo', 'Hoppingator', 
        'dearbornmusic', 'Slickdiscmusic', 'undergroundsoundsmi', 'TechniqueRecords', 
        'SweatRecords', 'Vinylasylum', 'Retrofit_Records', 'HearAgainRecords', 
        'groovyrecordsdeland', 'Ledzappa1956', 'secretsounds', 'Truetilldeathrecords', 
        'eraser.jax', 'tonevendor', 'deepthoughtsjp', 'GordonLaSalleVinyl', 
        'WantListRecords', 'planetrecords', 'armageddonshop', 'Villagevinylandhifi', 
        'WannaHearIt', 'lockedgroovellc', 'dj.mikie.love.s', 'normalsrecords', 
        'deepgroovesounds1', 'BabysOnFireBaltimore', 'JeffmanMusicEmporium', 
        'statestreetrecords', 'gethiprecordings', 'jerrysrecords', 'RevolverRecordsInc', 
        'blackdotsbuffalo', 'PrincetonRecordEx', 'recordrunnerusa', 'academyrecords', 
        'VinylFantasyBrooklyn', 'Factory-Record', 'humanheadnyc', 'JahAbrams', 
        'scottisrecordshop', 'recordgrouchbklyn', 'generationrecords', 
        'headsoundsrecords', 'facerecordsnyc', 'needleandgrooverec', 
        'RoughTradeNYC', 'MUSICONNECTION', 'longgoneday1', 'swoopy', 
        'Black_Gold_Brooklyn', 'Psychic_Brooklyn', 'almostready', 'ez2collect2', 
        'LooneyTunesCDs', 'justtracks', 'thevinylplant', 'DeepCutsRecordStore', 
        'hopfidelity', 'electric_avenue', 'ByrdlandRecords', 'Jointcustodydc', 'smashdc', 
        'RecordExchangeofSS', 'Mobius_Records', 'donutshoppe', 'IRREst.2022', 'thewaxhut', 
        'innergrooverecs', 'skyvalley420', 'timzatz', 'tunesonline', 'recordmuseum', 
        'phidelityrecords', 'Factory-Record', 'vinyl_dinosaur', 'clariziomusic', 
        'EastonExchange', 'doubledeckerrecords', 'RECREV', 'Young-Ones-Records', 
        'VertigoMusic449', 'WhitsEndTrading', 'impulsebuyrecords', 'dreaminghuman', 
        'Lititz_Music_Co.', 'MUSICALENERGIdotCOM', 'rebrecords-md', 'thevinylgarageus', 
        'admiralanalogs', 'FuzzyDogVintage', 'RecordExchangeofSS', 'YellowKShop', 
        'solarmountainrecords', 'recordsfromjupiter', 'rainbowrecordsde', 'extendedplay19971', 
        'philadelphiamusic', 'brewerytownbeats', 'creep-records', 'MilkcrateCafe', 'vinylaltar', 
        'commonbeatmusic', 'sitandspinrecords', 'Betternowrecords', 'impressionsphilly',
        'BullTrax', 'CTshop45s', 'bordentownrecords', 'pop.market', 'BrothersRecords',
        'VinylShopUS', 'kennyosrecords', 'stevierayvinyl', 'mhamilamelton' ,'dorightman',
        'recordsbymail', 'AlexanderCogs', 'Rose.Thyme', 'foreveryoungrecords', 'super.soul.records',
        'lewisdene', 'Niksvinyl', 'ShinylVinyl', 'CD_WAREHOUSE_817' ,'MRCLEANWAX',
        'ryanrecords', 'Boom_Service' ,'Armo-15' ,'Honeysmush_Records', 'GROOVEENT',
        'cjohnson22463', 'letitberarities', 'Kozuch438', 'Redscroll', 'kent221',
        'mstaurolite']

        for url in urls:
            for genre in genres:
                for seller in sellers:
                    urlnew = url + seller + '/profile?format=Vinyl' + genre
                    yield scrapy.Request(url=urlnew, callback=self.parse)


    def parse(self, response):
        listings = []
        for listing in response.xpath('//tr[@class="shortcut_navigable "]'):
            yield{
                'title' : response.xpath('//a[@class="item_description_title"]/text()').get(),
                'label' : response.xpath('//p[@class="hide_mobile label_and_cat"]/a/text()').get(),
                'itemCatNo' : response.xpath('//p[@class="hide_mobile label_and_cat"]/span[@class="item_catno"]/text()').get(),
                'sleeveCondition' : response.xpath('//span[@class="item_sleeve_condition"]/text()').get(),
                'rUrl' : response.xpath('//a[@class="item_release_link hide_mobile"]').attrib['href'],
                'lUrl' : response.xpath('//a[@class="item_description_title"]').attrib['href'],
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

