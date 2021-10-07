#This one was not provided in the report, but it was used for testing

import scrapy

import pandas as pd
import csv

IPdata = pd.read_csv(r'IP_list3.csv')

df_IPdata = pd.DataFrame(IPdata)
#
urls1 = df_IPdata['url']
urls1 = [i if i.startswith('http') else 'http://' + i for i in urls1]
urls1 = list(urls1)

class MySpider(scrapy.Spider):
    name = 'firstMalwareData'

    start_urls = urls1


    # for i in range(0, len(start_urls)):
    def parse(self, response):
            h1 = response.xpath("//h1").getall()
            div = response.xpath("//div").getall()
            url = response.url

            yield {'h1': h1,
                   'div': div,
                   'url': url}

