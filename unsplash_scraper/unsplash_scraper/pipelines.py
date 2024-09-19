import csv
from scrapy.pipelines.images import ImagesPipeline

class CsvPipeline:
    def open_spider(self, spider):
        self.file = open('images.csv', 'w', newline='', encoding='utf-8')
        self.exporter = csv.writer(self.file)
        self.exporter.writerow(['image_url', 'image_paths', 'title', 'category'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        image_path = item.get('image_paths', [''])[0]  # Получаем путь к изображению
        self.exporter.writerow([item['image_url'], image_path, item['title'], item['category']])
        return item
