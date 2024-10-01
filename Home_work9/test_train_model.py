from train_model import train_model, save_model
import pandas as pd
from sklearn.model_selection import train_test_split

# Создание тестового набора данных
data = {
    'reviewText': ['Отличный продукт', 'Плохое качество', 'Нормальный', 'Советую всем', 'Не рекомендую'],
    'sentiment': ['положительный', 'отрицательный', 'нейтральный', 'положительный', 'отрицательный']
}
df = pd.DataFrame(data)
X = df['reviewText']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Тестирование функции
model, vectorizer = train_model(X_train, y_train)
print("Модель обучена успешно!")
