import scrapy


class FlipSpider(scrapy.Spider):
    name = "flip"
    allowed_domains = ["flipkart.com"]
    start_urls = ["https://www.flipkart.com"]

    def parse(self, response):
        pass
