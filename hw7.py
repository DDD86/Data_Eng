from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Настройки ChromeDriver
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме
driver = webdriver.Chrome(options=options)

try:
    # Открываем сайт Quotes to Scrape
    driver.get("http://quotes.toscrape.com/")

    # Получаем страницы с цитатами
    quotes = []
    
    while True:
        # Ждем, пока элементы загрузятся
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote'))
        )

        # Извлекаем цитаты
        quote_elements = driver.find_elements(By.CLASS_NAME, 'quote')
        
        for quote in quote_elements:
            text = quote.find_element(By.CLASS_NAME, 'text').text.strip()
            author = quote.find_element(By.CLASS_NAME, 'author').text.strip()
            tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]
            quotes.append([text, author, ', '.join(tags)])

        # Переходим к следующей странице, если она существует
        next_button = driver.find_elements(By.LINK_TEXT, 'Next')
        if next_button:
            next_button[0].click()
        else:
            break

    # Открываем CSV для записи данных
    with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author', 'Tags'])  # Заголовки CSV файла

        # Записываем данные
        for quote in quotes:
            writer.writerow(quote)

    print("Данные успешно извлечены и сохранены в quotes.csv")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
