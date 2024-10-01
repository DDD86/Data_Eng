from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

import pandas as pd

def train_model(X_train, y_train):
    vectorizer = CountVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_train_vectorized, y_train)
    
    return model, vectorizer

def save_model(model, vectorizer):
    import joblib
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

if __name__ == "__main__":
    df = pd.read_csv('combined_labeled_reviews.csv')
    X = df['reviewText']
    y = df['sentiment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model, vectorizer = train_model(X_train, y_train)
    save_model(model, vectorizer)
