from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['books']
books = db.info

with open('books_data.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

books.insert_many(data)

books.update_one(
    {"title": "It's Only the Himalayas"},
    {"$set": {"price": "£50.00"}}
)
print("Цена книги обновлена.")

#книги, которые есть в наличии
# in_stock_books = books.find({"in_stock": {"$gt": 0}})
# for book in in_stock_books:
#     print(book)

count = books.count_documents({})
print("Количество книг в базе данных:", count)

# # Сортировка книг по цене
# sorted_books = books.find().sort("price", 1)  # 1 для сортировки по возрастанию
# for book in sorted_books:
#     print(book)

title_to_search = "B"
book = books.find_one({"title": {"$regex": f"^{title_to_search}"}}, {"_id": 0, "title": 1})

if book:
    print("Найдена книга:", book)
else:
    print("Книга не найдена.")