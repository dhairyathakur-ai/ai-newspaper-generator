import os
import csv
from datetime import datetime

from flask import Flask, render_template, request
from src.summarizer import generate_summary

app = Flask(__name__)

HISTORY_FILE = "dataset/generated_news.csv"

FIELDNAMES = [
    "headline",
    "article",
    "category",
    "summary",
    "date"
]

categories = [
    "Technology",
    "Sports",
    "Business",
    "Politics",
    "Science",
    "Entertainment",
    "Education",
    "Health"
]


# Initialize and migrate CSV
def initialize_history():

    os.makedirs("dataset", exist_ok=True)

    if not os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

        return

    with open(HISTORY_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        return

    header = rows[0]
    migrated_rows = []

    for row in rows[1:]:

        if len(row) == 5:
            # Records saved using the newer code:
            # headline, category, article, summary, date

            migrated_rows.append({
                "headline": row[0],
                "article": row[2],
                "category": row[1],
                "summary": row[3],
                "date": row[4]
            })

        elif len(row) == 4:
            # Original CSV structure

            migrated_rows.append({
                "headline": row[0],
                "article": row[1],
                "category": row[2],
                "summary": row[3],
                "date": ""
            })

    with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(migrated_rows)

# Load news and remove existing duplicate headlines
def load_news():

    initialize_history()

    with open(HISTORY_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        all_news = list(reader)

    unique_news = []
    seen_headlines = set()

    # Start from newest records
    for news in reversed(all_news):

        headline = news["headline"].strip()

        # Normalize headline for comparison
        normalized = " ".join(headline.casefold().split())

        if normalized and normalized not in seen_headlines:

            seen_headlines.add(normalized)
            unique_news.append(news)

    # Restore original order
    unique_news.reverse()

    # Rewrite CSV without duplicate records
    if len(unique_news) != len(all_news):

        with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

            writer.writeheader()
            writer.writerows(unique_news)

        print("Duplicate news removed successfully!")

    return unique_news

# Prevent duplicate headlines
def headline_exists(headline):

    all_news = load_news()

    return any(
        news["headline"].strip().lower() == headline.strip().lower()
        for news in all_news
    )


# Save generated news
def save_news(headline, category, article, summary):

    if headline_exists(headline):
        return False

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writerow({
            "headline": headline,
            "article": article,
            "category": category,
            "summary": summary,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M")
        })

    return True


# Homepage
@app.route("/", methods=["GET", "POST"])
def home():

    headline = ""
    article = ""
    category = ""
    summary = ""
    message = ""

    if request.method == "POST":

        headline = request.form.get("headline", "").strip()
        article = request.form.get("article", "").strip()
        category = request.form.get("category", "").strip()

        if headline and article and category:

            if headline_exists(headline):

                message = "This headline already exists in your newspaper archive."

            else:

                summary = generate_summary(article)

                save_news(
                    headline,
                    category,
                    article,
                    summary
                )

    return render_template(
        "newspaper.html",
        headline=headline,
        article=article,
        category=category,
        categories=categories,
        summary=summary,
        message=message
    )


# Search News
@app.route("/search")
def search():

    query = request.args.get("q", "").strip().lower()

    all_news = load_news()

    if query:

        results = [
            news for news in all_news
            if query in news["headline"].lower()
            or query in news["category"].lower()
            or query in news["summary"].lower()
        ]

    else:
        results = []

    return render_template(
        "search.html",
        results=results,
        query=query
    )


# Newspaper Edition
@app.route("/edition")
def newspaper_edition():

    articles = load_news()

    articles.reverse()

    edition_date = datetime.now().strftime("%A, %d %B %Y")

    return render_template(
        "newspaper_edition.html",
        articles=articles,
        edition_date=edition_date
    )


if __name__ == "__main__":

    app.run(debug=True)