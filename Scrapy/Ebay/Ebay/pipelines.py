# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class EbayPipeline(object):
#     def process_item(self, item, spider):
#         return item
from scrapy import signals
from scrapy.exporters import CsvItemExporter


class MyCsvItemExporter(CsvItemExporter):

    def __init__(self, file, **kwargs):
        kwargs['delimiter'] = ';'
        super().__init__(file, **kwargs)


class EbayPipeline(object):

    def __init__(self):
        self.exporter = None
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = MyCsvItemExporter(file=file)
        self.exporter.fields_to_export = (
            'ID', 'Title', 'Price', 'Postage', 'Sell_Date', 'Location', 'Condition',
            'Product_Type', 'Product_Line', 'Brand', 'Screen_Size', 'Screen_Resolution',
            'Storage_Type', 'Storage_Capacity', 'Model', 'Operating_System', 'Operating_System_Edition',
            'RAM_Memory', 'Processor', 'Processor_Speed', 'Seller', 'Seller_Notes', 'URL'
        )
        self.exporter.encoding = 'utf-8'
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        print(spider)  # nepodstatny riadok, len aby pyCharm neukazoval ze input arg "spider" sa nepouziva
        self.exporter.export_item(item)
        return item
