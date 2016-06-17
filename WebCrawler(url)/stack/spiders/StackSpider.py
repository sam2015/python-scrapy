from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field

class MyItem(Item):
    url= Field()


class someSpider(CrawlSpider):
    name = 'crawltest'
    allowed_domains = ['www.cinemax-prod.co.il']
    start_urls = ['http://www.cinemax-prod.co.il/index.asp']
    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def parse_obj(self,response):
        item = MyItem()
        item['url'] = []
        for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
            item['url'].append(link.url)
        return item