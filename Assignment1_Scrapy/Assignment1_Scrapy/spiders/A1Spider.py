import re
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class A1_Spider(CrawlSpider):
    name = "A1Spider"
    allowed_domains = ["kennesaw.edu"]
    start_urls = ["https://www.kennesaw.edu/"]

    rules = (
        Rule(LinkExtractor(allow=('kennesaw.edu',)), callback='parse_items'),
    )


    def parse_items(self, response):
        entry = dict.fromkeys(['pageid', 'url', 'title', 'body', 'emails'])

        # Extracting pageid from the URL or response
        entry['pageid'] = hash(response.url)

        # Extracting URL
        entry['url'] = response.url

        # Extracting title
        entry['title'] = response.css('title::text').get()

        # Extracting body using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        entry['body'] = soup.get_text()

        # Extracting emails using regular expression
        email_pattern = r'[\w\.-]+@[\w\.-]+'
        entry['emails'] = re.findall(email_pattern, response.text)

        yield entry
