import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class A1_Spider(CrawlSpider):
    name = "A1Spider"
    allowed_domains = ["kennesaw.edu"]
    start_urls = ["https://www.kennesaw.edu/"]

    rules = (
        Rule(LinkExtractor(allow=('/page/\d+',)), callback='parse_items'),
    )

    def parse_items(self, response):
        entry = dict.fromkeys(['pageid', 'url', 'title', 'body', 'emails'])

        # Extracting pageid from the URL or response
        entry['pageid'] = re.search(r'/page/(\d+)/', response.url).group(1)

        # Extracting URL
        entry['url'] = response.url

        # Extracting title
        entry['title'] = response.css('title::text').get()

        # Extracting body
        entry['body'] = ' '.join(response.css('body p::text').getall())

        # Extracting emails using regular expression
        email_pattern = r'[\w\.-]+@[\w\.-]+'
        entry['emails'] = re.findall(email_pattern, response.text)

        yield entry
