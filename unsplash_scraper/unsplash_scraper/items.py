import scrapy

class UnsplashImageItem(scrapy.Item):
    image_url = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    image_paths = scrapy.Field()  # Поле для хранения пути после загрузки
