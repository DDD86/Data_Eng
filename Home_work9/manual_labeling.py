import pandas as pd

def merge_datasets(auto_file, manual_file):
    df_auto = pd.read_csv(auto_file)
    df_manual = pd.read_csv(manual_file)
    df_combined = pd.concat([df_auto, df_manual], ignore_index=True)
    return df_combined

if __name__ == "__main__":
    df_combined = merge_datasets('auto_labeled_reviews.csv', 'manual_labeled_reviews.csv')
    df_combined.to_csv('combined_labeled_reviews.csv', index=False)
