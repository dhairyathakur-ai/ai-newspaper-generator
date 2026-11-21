from headline_processor import load_news_data, process_news
from summarizer import generate_summary


print("Loading News Dataset...")

# Load and clean dataset
df = load_news_data()
df = process_news(df)

print("\nGenerating AI Summaries...\n")

# Generate summary for every article
df["summary"] = df["article"].apply(generate_summary)


# Display newspaper content
for index, row in df.iterrows():

    print("=" * 60)

    print("HEADLINE:", row["headline"])

    print("\nCATEGORY:", row["category"])

    print("\nSUMMARY:", row["summary"])

    print("=" * 60)


# Save generated newspaper data
df.to_csv("dataset/generated_news.csv", index=False)

print("\nNewspaper data saved successfully!")