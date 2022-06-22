import os
import scrapy

class MlSpider(scrapy.Spider):
    json = 'data.json'
    if os.path.exists(json) == True:
        os.remove(json)
        
    name = 'ml'
    start_urls = [f'https://www.mercadolivre.com.br/ofertas?page={i}' for i in range(1, 6)]

    def parse(self, response):
        
        for i in response.xpath('//ol[@class="items_container"]'):
            price = i.xpath('.//span[@class="promotion-item__price"]//text()').getall()
            title = i.xpath('.//p[@class="promotion-item__title"]/text()').getall()
            link = i.xpath('.//a[@class="promotion-item__link-container"]/@href').getall()
        yield{
            'Price':price,
            'Title':title,
            'Link':link
        }