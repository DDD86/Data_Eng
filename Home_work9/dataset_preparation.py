import pandas as pd

def load_dataset():
    df = pd.read_csv('amazon_reviews.csv')
    return df

def save_dataset(df, filename):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    df = load_dataset()
    save_dataset(df, 'prepared_reviews.csv')
