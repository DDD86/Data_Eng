import requests
from lxml import html
import csv

url = "https://ru.wikipedia.org/wiki/Список_стран_по_ВВП_(номинал)"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    page_content = response.content

    tree = html.fromstring(page_content)

    rows = tree.xpath('//table[contains(@class,"wikitable")]//tr')

    with open('gdp_countries.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for row in rows:
            data = row.xpath('.//th//text() | .//td//text()')

            data = [item.strip() for item in data if item.strip()]
            
            if data:
                writer.writerow(data)

    print("Данные успешно сохранены в файл gdp_countries.csv")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении HTTP-запроса: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
