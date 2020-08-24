# -*- coding: utf-8 -*-
import scrapy


class YaleSpider(scrapy.Spider):
    name = 'yale'
    allowed_domains = ['covid19.yale.edu']
    start_urls = ['https://covid19.yale.edu/yale-covid-19-statistics']

    def parse(self, response):
        # cases_since_may_20 = "/html/body/div[3]/main/div/div[2]/div/div[3]/div/div/div/div/article/div[1]/div/div/div/table/tbody/tr[3]/td[6]/strong"
        yield {"RecentCases": response.selector.xpath('//*[text() = "Total"]/../../td[7]//strong/text()').get()[:-1]}
