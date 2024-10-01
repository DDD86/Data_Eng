from dataset_preparation import load_dataset, save_dataset
from rule_based_labeling import apply_rule_based_labeling
from manual_labeling import merge_datasets
import train_model
from evaluate_model import evaluate_model
import pandas as pd
from sklearn.model_selection import train_test_split

def train_and_evaluate_model(df):
    # Обучение модели
    X = df['reviewText']
    y = df['sentiment']
    
    # Проверка на наличие NaN перед разделением
    print("Проверка на NaN в X:")
    print(X.isnull().sum())
    print("Проверка на NaN в y:")
    print(y.isnull().sum())

    # Разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Обучение модели
    model, vectorizer = train_model.train_model(X_train, y_train)
    train_model.save_model(model, vectorizer)

    # Оценка модели
    evaluate_model(X_test, y_test)

# Загрузка и подготовка датасета
df = load_dataset()
save_dataset(df, 'prepared_reviews.csv')

# Разметка на основе правил
df = apply_rule_based_labeling(df)
df.to_csv('auto_labeled_reviews.csv', index=False)

# Объединение с ручной разметкой
df_combined = merge_datasets('auto_labeled_reviews.csv', 'manual_labeled_reviews.csv')

# Удаление или заполнение NaN
df_combined.dropna(subset=['reviewText', 'sentiment'], inplace=True)
df_combined.to_csv('combined_labeled_reviews.csv', index=False)

# Обучение и оценка модели
train_and_evaluate_model(df_combined)
