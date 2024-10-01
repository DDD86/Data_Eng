import pandas as pd

# Пример данных для создания файла
data = {
    'reviewText': ['Это отличный продукт!', 'Не очень понравился', 'Просто нормально'],
    'sentiment': ['положительный', 'отрицательный', 'нейтральный']
}

df_manual = pd.DataFrame(data)
df_manual.to_csv('manual_labeled_reviews.csv', index=False)
