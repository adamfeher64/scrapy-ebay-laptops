import scrapy
from scrapy import Spider
from ..items import EbayProductItem


class EbaySpider(Spider):
    id = 0
    name = 'Ebay'
    keyword = 'laptop+i7+16gb'
    start_urls = (
        "https://www.ebay.co.uk/sch/i.html?LH_Complete=1&LH_Sold=1&_sop=13&LH_BIN=1&_nkw={0}".format(keyword),
    )

    def parse(self, response):
        links = response.css('a.vip::attr(href)').getall()
        i = 0
        for link in links:
            abs_url = response.urljoin(link)
            title = response.css('a.vip::attr(title)')[i].get()
            title = title.replace('Click this link to access ', '')
            date = response.css('span.tme').xpath("child::span").xpath('normalize-space(text())').get()
            i += 1
            yield scrapy.Request(
                url=abs_url,
                callback=self.parse_original,
                meta={'title': title, 'date': date}
            )
        next_page = response.css('a.gspr.next::attr(href)').get()
        yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_original(self, response):
        old_url = response.url
        new_url = response.css('a:contains("See original listing")::attr(href)').get()
        title = response.meta['title']
        date = response.meta['date']
        if new_url:
            yield scrapy.Request(
                url=new_url,
                callback=self.parse_items,
                meta={'title': title, 'date': date}
            )
        else:
            yield scrapy.Request(
                url=old_url,
                callback=self.parse_items,
                meta={'title': title, 'date': date},
                dont_filter=True
            )

    def parse_items(self, response):
        self.id += 1
        item = EbayProductItem()

        # Price
        price = response.xpath('//span[@itemprop="price" or @id="prcIsum"]')
        price = price.xpath('normalize-space(text())').get()
        if price:
            price = price.split('£', 1)[1]
            price = price.split(' each', 1)[0]
            price = price.replace(',', '')
        else:
            price = None

        # Postage
        postage = response.css('span#fshippingCost span')
        postage = postage.xpath('normalize-space(text())').get()
        if postage:
            postage = postage.split('£', 1)[1]
            postage = postage.replace(',', '')
        else:
            postage = None

        # Location
        location = response.css('span[itemprop="availableAtOrFrom"]')
        location = location.xpath('normalize-space(text())').get()
        if location:
            location = location
        else:
            location = None

        # Condition
        condition = response.css('div[itemprop="itemCondition"]')
        condition = condition.xpath('normalize-space(text())').get()
        if condition:
            condition = condition.replace('–', '-')
        else:
            condition = None

        # Product Type
        product_type = response.xpath('//td['
                                      'text()="\n\t\t\t\t\t\t\t\t\t \t\t\tType: "'
                                      ' or '
                                      'text()="\n\t\t\t\t\t\t\t\t\t \t\t\tProduct Type: "]')
        product_type = product_type.xpath('following-sibling::td/span')
        product_type = product_type.xpath('normalize-space(text())').get()
        if product_type:
            product_type = product_type
        else:
            product_type = None

        # Product Line
        product_line = response.xpath('//td[contains(text(), "Product Line:")]')
        product_line = product_line.xpath('following-sibling::td/span')
        product_line = product_line.xpath('normalize-space(text())').get()
        if product_line:
            product_line = product_line
        else:
            product_line = None

        # Brand
        brand = response.xpath('//td['
                               'text()="\n\t\t\t\t\t\t\t\t\t \t\t\tBrand: "'
                               ' or '
                               'text()="\n\t\t\t\t\t\t\t\t\t \t\t\tbrand: "]')
        brand = brand.xpath('following-sibling::td/span')
        brand = brand.xpath('normalize-space(text())').get()
        if brand:
            brand = brand
        else:
            brand = None

        # Screen Size
        screen_size = response.xpath('//td[contains(text(), "Screen Size:")]')
        screen_size = screen_size.xpath('following-sibling::td/span')
        screen_size = screen_size.xpath('normalize-space(text())').get()
        if brand:
            screen_size = screen_size
        else:
            screen_size = None

        # Screen Resolution
        screen_resolution = response.xpath('//td[contains(text(), "Resolution:")]')
        screen_resolution = screen_resolution.xpath('following-sibling::td/span')
        screen_resolution = screen_resolution.xpath('normalize-space(text())').get()
        if screen_resolution:
            screen_resolution = screen_resolution
        else:
            screen_resolution = None

        # Storage Type
        storage_type = response.xpath('//td[contains(text(), "Storage Type:")]')
        storage_type = storage_type.xpath('following-sibling::td/span')
        storage_type = storage_type.xpath('normalize-space(text())').get()
        if storage_type:
            storage_type = storage_type
        else:
            storage_type = None

        # Storage Capacity
        storage_capacity = response.xpath('//td[contains(text(), "Hard Drive Capacity:")]')
        storage_capacity = storage_capacity.xpath('following-sibling::td/span')
        storage_capacity = storage_capacity.xpath('normalize-space(text())').get()
        if storage_capacity == 'Not Applicable':
            storage_capacity = response.xpath('//td[contains(text(), "SSD Capacity:")]')
            storage_capacity = storage_capacity.xpath('following-sibling::td/span')
            storage_capacity = storage_capacity.xpath('normalize-space(text())').get()
        else:
            storage_capacity = None

        # Model
        model = response.css('td:contains("Model:")')
        model = model.xpath('following-sibling::td/span')
        model = model.xpath('normalize-space(text())').get()
        if model:
            model = model
        else:
            model = None

        # Operating System
        operating_system = response.css('td:contains("Operating System:")')
        operating_system = operating_system.xpath('following-sibling::td/span')
        operating_system = operating_system.xpath('normalize-space(text())').get()
        if operating_system:
            operating_system = operating_system
        else:
            operating_system = None

        # Operating System
        operating_system_edition = response.css('td:contains("Operating System Edition:")')
        operating_system_edition = operating_system_edition.xpath('following-sibling::td/span')
        operating_system_edition = operating_system_edition.xpath('normalize-space(text())').get()
        if operating_system_edition:
            operating_system_edition = operating_system_edition
        else:
            operating_system_edition = None

        # RAM Memory
        ram_memory = response.xpath('//td[contains(text(), "RAM")]')
        ram_memory = ram_memory.xpath('following-sibling::td/span')
        ram_memory = ram_memory.xpath('normalize-space(text())').get()
        if ram_memory:
            ram_memory = ram_memory
        else:
            ram_memory = None

        # Processor
        processor = response.xpath('//td[contains(text(), "Processor:") or contains(text(), "Processor Type:")]')
        processor = processor.xpath('following-sibling::td/span')
        processor = processor.xpath('normalize-space(text())').get()
        if processor:
            processor = processor
        else:
            processor = None

        # Processor Speed
        processor_speed = response.xpath('//td[contains(text(), "Processor Speed:")]')
        processor_speed = processor_speed.xpath('following-sibling::td/span')
        processor_speed = processor_speed.xpath('normalize-space(text())').get()
        if processor_speed:
            processor_speed = processor_speed
        else:
            processor_speed = None

        # Seller
        seller = response.css('span.mbg-nw')
        seller = seller.xpath('normalize-space(text())').get()
        if seller:
            seller = seller
        else:
            seller = None

        # Seller Notes
        seller_notes = response.css('span.viSNotesCnt')
        seller_notes = seller_notes.xpath('normalize-space(text())').get()
        if seller_notes:
            seller_notes = seller_notes
        else:
            seller_notes = None

        # Output
        item['ID'] = self.id
        item['Title'] = response.meta['title']
        item['Price'] = price
        item['Postage'] = postage
        item['Sell_Date'] = response.meta['date']
        item['Location'] = location
        item['Condition'] = condition
        item['Product_Type'] = product_type
        item['Product_Line'] = product_line
        item['Brand'] = brand
        item['Screen_Size'] = screen_size
        item['Screen_Resolution'] = screen_resolution
        item['Storage_Type'] = storage_type
        item['Storage_Capacity'] = storage_capacity
        item['Model'] = model
        item['Operating_System'] = operating_system
        item['Operating_System_Edition'] = operating_system_edition
        item['RAM_Memory'] = ram_memory
        item['Processor'] = processor
        item['Processor_Speed'] = processor_speed
        item['Seller'] = seller
        item['Seller_Notes'] = seller_notes
        item['URL'] = response.url
        yield item
