import pandas as pd

path1 = 'C:/Users/Lenovo/Desktop/Ebay Scraping Project/Scrapy/Ebay/Title_URL.csv'
path2 = 'C:/Users/Lenovo/Desktop/Ebay Scraping Project/Scrapy/Ebay/Scraping_Items.csv'

t1 = pd.read_csv(filepath_or_buffer=path1, sep=';')
t2 = pd.read_csv(filepath_or_buffer=path2, sep=';')
t1.join(t2, how='inner', sort=['ID'], lsuffix='1')
print(t1)
