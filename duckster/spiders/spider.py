import re
import json
import urllib

from pprint import pprint


from scrapy.selector import Selector
# try:
from scrapy.spiders import Spider
# except:
#     from scrapy.spiders import BaseSpider as Spider
# from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle


from duckster.items import jokeItem

import pprint


class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        # if isinstance(object, unicode):
        #     return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)


class ducksterSpider(Spider):
    name = "duckster"
    allowed_domains = ["www.ducksters.com"]
    start_urls = [
        "https://www.ducksters.com/jokes"
    ]

    rules = [
        Rule(sle(allow=("/jokes/*")),
             callback='parse', follow=True),
    ]

    def parse(self, response):

        links = response.css("a::attr(href)")
        for link in links:
            if "jokes" in link.get():
                yield response.follow(link, self.parse)

        text = response.xpath("string()").extract()[0]

        lines = text.split("\n")
        question = None
        answer = None
        for line in lines:
            if len(line) == 0:
                continue
            if "Q:" in line:
                question = line
                continue

            if "A:" in line:
                answer = line

            if question is not None and line is not None:

                yield jokeItem(question=question, answer=answer)
                question = None
                answer = None
