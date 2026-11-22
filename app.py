from flask import Flask, render_template, request
from src.summarizer import generate_summary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    headline = ""
    article = ""
    category = ""
    summary = ""

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

    if request.method == "POST":

        headline = request.form["headline"]
        article = request.form["article"]
        category = request.form["category"]

        if headline.strip() and article.strip():
            summary = generate_summary(article)

    return render_template(
        "newspaper.html",
        headline=headline,
        article=article,
        category=category,
        categories=categories,
        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)