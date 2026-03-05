
import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.loader import ItemLoader
from laptop.items import LaptopItem



class GetlpSpider(scrapy.Spider):
    name = "getlp"
    allowed_domains = ["www.flipkart.com"]
    start_urls = ["https://www.flipkart.com"]

    def start_requests(self):
        # GET request
        yield scrapy.Request(self.start_urls[0], 
                             meta={
                                 "playwright": True,
                                 "playwright_page_methods": [
                                    PageMethod("wait_for_load_state", "domcontentloaded"),
                                    PageMethod("wait_for_timeout", 2000),
                                    PageMethod("click", 'span[role="button"].b3wTlE'),
                                    PageMethod("wait_for_timeout", 2000),
                                    PageMethod("fill","div.olwU0Z.CXZSEo input.nw1UBF.v1zwn25","laptop"),
                                    PageMethod("wait_for_timeout", 2000),
                                    PageMethod("click",'div.olwU0Z.CXZSEo button.XFwMiH'),
                                    PageMethod("wait_for_timeout", 2000),
                                    PageMethod("wait_for_load_state", "networkidle"),
                                    PageMethod("wait_for_load_state", "domcontentloaded"),
                                    PageMethod("wait_for_load_state", "load"),
PageMethod("screenshot", path="lp1.png", full_page=True)                                 ]
                                 }
                                 )
      

    def parse(self, response):
        laptops = response.css("div.lvJbLV.col-12-12 div.jIjQ8S")
       
        for laptop in laptops:
            #l = ItemLoader(item=LaptopItem(), selector=laptop)
            title = laptop.css("div.RG5Slk::text").get()

            name = title.split("-")[0].strip() if title else None
            details = title.split("-")[1].strip() if "-" in title else None
            LaptopItemloader = ItemLoader(item=LaptopItem(), selector=laptop)

            LaptopItemloader.add_value("name", name)
            LaptopItemloader.add_value("details", details)
            
            LaptopItemloader.add_css("original_price", "div.kRYCnD.gxR4EY::text")
            LaptopItemloader.add_css("discount", "div.HQe8jr span::text")
            LaptopItemloader.add_css("final_price", "div.hZ3P6w.DeU9vF::text")
            LaptopItemloader.add_css("rating", "div.ZFwe0M.row > div.col-7-12 .MKiFS6::text")
            
            yield LaptopItemloader.load_item()

            # lp = {
            #     "name": laptop.css("div.RG5Slk::text").get(),
            #     "price": laptop.css("div.hZ3P6w.DeU9vF::text").get(),
            #     "rating": laptop.css("div.ZFwe0M.row > div.col-7-12 .MKiFS6::text").get(),
            # }
           
            # yield lp
        next_page = response.css("a.jgg0SZ::attr(href)").get()

        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse,
                meta={"playwright": True}
            )
