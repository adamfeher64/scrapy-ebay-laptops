# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EbayProductItem(scrapy.Item):
    ID = scrapy.Field()
    Title = scrapy.Field()
    Price = scrapy.Field()
    Postage = scrapy.Field()
    Sell_Date = scrapy.Field()
    Location = scrapy.Field()
    Condition = scrapy.Field()
    Product_Type = scrapy.Field()
    Product_Line = scrapy.Field()
    Brand = scrapy.Field()
    Screen_Size = scrapy.Field()
    Screen_Resolution = scrapy.Field()
    Storage_Type = scrapy.Field()
    Storage_Capacity = scrapy.Field()
    Model = scrapy.Field()
    Operating_System = scrapy.Field()
    Operating_System_Edition = scrapy.Field()
    RAM_Memory = scrapy.Field()
    Processor = scrapy.Field()
    Processor_Speed = scrapy.Field()
    Seller = scrapy.Field()
    Seller_Notes = scrapy.Field()
    URL = scrapy.Field()
    pass

