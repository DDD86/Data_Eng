import requests
from bs4 import BeautifulSoup
import json

base_url = 'http://books.toscrape.com/'

def get_book_info(book_url):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.h1.text
    price = soup.find('p', class_='price_color').text
    
    # Извлечение количества книг в наличии
    in_stock_text = soup.find('p', class_='instock availability').text.strip()
    # Удаляем все символы, кроме цифр
    in_stock = int(''.join(filter(str.isdigit, in_stock_text)))

    description_tag = soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'].strip() if description_tag else 'No description available'
    
    return {
        'title': title,
        'price': price,
        'in_stock': in_stock,
        'description': description
    }


def get_books_from_category(category_url):
    books = []
    while category_url:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        book_links = [base_url + 'catalogue/' + a['href'].replace('../../../', '') for a in soup.select('h3 > a')]
        for book_link in book_links:
            book_info = get_book_info(book_link)
            books.append(book_info)
        
        next_page = soup.find('li', class_='next')
        category_url = base_url + next_page.a['href'] if next_page and next_page.a else None

    return books

def get_all_categories():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    categories = []
    
    category_elements = soup.select('div.side_categories ul li ul li a')
    for category in category_elements:
        if category and category['href']:
            category_links = base_url + category['href']
            categories.append(category_links)
    
    return categories

def scrape_books_to_json():
    categories = get_all_categories()
    all_books = []
    
    for category_url in categories:
        category_books = get_books_from_category(category_url)
        all_books.extend(category_books)
    
    with open('books_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_books, f, ensure_ascii=False, indent=4)

scrape_books_to_json()
