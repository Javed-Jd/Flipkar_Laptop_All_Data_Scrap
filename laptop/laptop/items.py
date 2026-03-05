# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
import re

def cleanprice(price):
    print('cleaning price:')
    print(price)
    print('cline price done')

    if not price:
        return 0.0
    
    # Remove currency symbols and text, keep numbers and commas
    cleaned = re.sub(r"[^\d,\.]", "", price)
    
    # Remove commas
    cleaned = cleaned.replace(",", "")
    
    # Convert to float
    return float(cleaned)

class LaptopItem(scrapy.Item):

    name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    details = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    original_price = scrapy.Field(
        input_processor=MapCompose(cleanprice),
        output_processor=TakeFirst()
    )

    discount = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    final_price = scrapy.Field(
        input_processor=MapCompose(cleanprice),
        output_processor=TakeFirst()
    )

    rating = scrapy.Field(
        input_processor=MapCompose(float),
        output_processor=TakeFirst()
    )


# class LaptopItem(scrapy.Item):
#     # define the fields for your item here like:
#     name = scrapy.Field(
#         input_processor = MapCompose(str.strip),
#         output_processor = TakeFirst()
#     )
#     price = scrapy.Field(
#         input_processor = MapCompose(cleanprice),
#         output_processor = TakeFirst()
#     )
#     rating = scrapy.Field(
#         input_processor = MapCompose(float),
#         output_processor = TakeFirst()
#     )
#     pass
