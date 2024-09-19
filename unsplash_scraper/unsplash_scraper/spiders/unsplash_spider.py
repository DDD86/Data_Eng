import scrapy
from unsplash_scraper.items import UnsplashImageItem
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from unsplash_scraper.items import UnsplashImageItem


class UnsplashSpider(scrapy.Spider):
    name = 'unsplash_spider'
    allowed_domains = ['unsplash.com']
    start_urls = ['https://unsplash.com']

    def parse(self, response):
        # Adjust selectors based on the actual HTML structure of Unsplash
        for image in response.css('figure'):
            item = UnsplashImageItem()
            item['url'] = image.css('img::attr(src)').get()
            item['title'] = image.css('img::attr(alt)').get()
            # Add 'category' if applicable
            yield item



    def parse_category(self, response):
        # Обновленные селекторы для изображений в категории
        images = response.css('figure img')
        for image in images:
            image_url = image.css('::attr(src)').get()
            image_title = image.css('::attr(alt)').get() or "No title"
            category = response.url.split('/')[-1]  # Категория из URL

            # Создание элемента Scrapy
            yield UnsplashImageItem(
                image_url=image_url,
                title=image_title,
                category=category
            )
        
        # Переход на следующую страницу категории
        next_page = response.css('a[data-test="pagination-link-next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse_category)
