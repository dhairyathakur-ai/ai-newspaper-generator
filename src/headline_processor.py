import pandas as pd
import re


def load_news_data():
     
    df = pd.read_csv("dataset/news.csv")

    print("Dataset Loaded Successfully!")
    print("\nDataset Shape:", df.shape)
    print("\nAvailable Columns:", df.columns.tolist())

    return df


def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def process_news(df):
    # Remove rows with missing values
    df = df.dropna()

    # Clean headlines and articles
    df["headline"] = df["headline"].apply(clean_text)
    df["article"] = df["article"].apply(clean_text)

    return df


if __name__ == "__main__":

    news = load_news_data()

    news = process_news(news)

    print("\nProcessed News:")
    print(news.head())