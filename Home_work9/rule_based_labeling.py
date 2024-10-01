import pandas as pd

def sentiment_label(rating):
    if rating >= 4:
        return 'положительный'
    elif rating <= 2:
        return 'отрицательный'
    else:
        return 'нейтральный'

def apply_rule_based_labeling(df):
    df['sentiment'] = df['overall'].apply(sentiment_label)
    return df

if __name__ == "__main__":
    df = pd.read_csv('prepared_reviews.csv')
    df = apply_rule_based_labeling(df)
    df.to_csv('auto_labeled_reviews.csv', index=False)
