## Summary
A simple project designed in Python using the Scrapy library. Based on any search query, it stores records of all recently sold laptops on the well-known Ebay online store. The best results will be achieved if the search query is related to laptops. The process takes approximately 7 minutes. The result of the scraping process is a csv file containing a table of records that will be saved to local storage.

### Instructions:
1. In the PyCharm Terminal (not in the Python Console!) you enter the ../Scrapy/Ebay folder via the "cd" command
2. Type "scrapy crawl Ebay" and after about 7 minutes you will generate Ebay_items.csv
3. ???
4. Profit

### List of CSV items (columns):
- ID
- Title
- Price
- Postage
- Sell_Date
- Location
- Condition
- Product_Type
- Product_Line
- Brand
- Screen_Size
- Screen_Resolution
- Storage_Capacity
- Model
- Operating_System
- Operating_System_Edition
- RAM_Memory
- Processor
- Processor_Speed
- Seller
- Seller_Notes
- URL

### Preview (first 7 columns):
![Preview](https://i.imgur.com/DBVDtef.png)
