# -*- coding: utf-8 -*-
import scrapy
from meishitianxia.items import MeishitianxiaItem

class TiantianmeishiSpider(scrapy.Spider):
    name = "meishitianxia"
    allowed_domains = ["meishichina.com"]
    start_urls = ['http://home.meishichina.com/recipe-list.html']

    def parse(self, response):
        
        nodes=response.xpath('//li[@data-id]')
        for node in nodes:    
            recipe=MeishitianxiaItem()
            recipe['recipe_name']=node.xpath('div[@class="detail"]/h2/a[@target="_blank"]/text()').extract_first()
            recipe['ingredients']=node.xpath('div[@class="detail"]/p[@class="subcontent"]/text()').extract_first()
            print(recipe['recipe_name'])
            yield recipe
        next_page=response.xpath('//div[@class="ui-page mt10"]//@href').extract()[-1]
        yield scrapy.Request(next_page,callback=self.parse)
        
        