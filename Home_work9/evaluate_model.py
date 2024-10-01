import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib

def evaluate_model(X_test, y_test):
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    X_test_vectorized = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_vectorized)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    df = pd.read_csv('combined_labeled_reviews.csv')
    X = df['reviewText']
    y = df['sentiment']

    from sklearn.model_selection import train_test_split
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    evaluate_model(X_test, y_test)
