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
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_text = ' '.join([str(tag) for tag in soup.find_all()])
        entry['emails'] = re.findall(regex, email_text)
        yield entry
