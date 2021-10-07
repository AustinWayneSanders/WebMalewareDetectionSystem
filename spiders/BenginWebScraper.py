# This one is used in the report for scraping benign web sites

import scrapy

import pandas as pd
import csv

IPdata = pd.read_csv(r'/home/austin/top500Domains.csv')

df_IPdata = pd.DataFrame(IPdata)
#
urls1 = df_IPdata['Root Domain']
urls1 = [i if i.startswith('http') else 'http://' + i for i in urls1]
urls1 = list(urls1)

class MySpider(scrapy.Spider):
    name = 'BenignWebCrawler'

    start_urls = urls1

    def parse(self, response):

            h1 = response.xpath("//h1").getall()
            url = response.url

            yield {'h1': h1,
                   'url': url}

# To run this crawler, change directory to the directory with this file and type: scrapy crawl BeninWebCralwer in the terminal