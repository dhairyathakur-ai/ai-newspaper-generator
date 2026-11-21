# 📰 AI Newspaper Generator

An AI-powered newspaper generation application built using Python, Flask, and Hugging Face Transformers.

The application allows users to enter a news headline and its source article. An AI summarization model processes the provided article and generates a concise news summary, which is displayed on a newspaper-style webpage.

---

## 🚀 Project Overview

The **AI Newspaper Generator** aims to simplify news presentation using Artificial Intelligence.

Instead of manually summarizing long news articles, users can provide a headline and article text, and the application automatically generates a shorter, readable summary.

The project combines Natural Language Processing (NLP), AI summarization, and web development to create an interactive news-generation experience.

---

## ✨ Features

- 📝 **Headline Input:** Enter your own news headline.
- 📄 **Article Input:** Provide the original news article or source text.
- 🤖 **AI Summarization:** Generate concise summaries using a pretrained Hugging Face model.
- 🌐 **Web Interface:** Interact with the application through a Flask-powered website.
- 📰 **Newspaper Layout:** Display generated news in a newspaper-style interface.
- 📊 **Dataset Processing:** Load, clean, and process news data using Pandas.
- ⚡ **Automated Processing:** Generate summaries without manually writing them.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Hugging Face Transformers | AI summarization |
| PyTorch | Deep learning framework |
| Pandas | Dataset processing |
| HTML5 | Webpage structure |
| CSS3 | Website styling |
| Git & GitHub | Version control |

### AI Model

The project currently uses:

`sshleifer/distilbart-cnn-12-6`

This is a pretrained DistilBART model designed for text summarization.

---

## 📂 Project Structure

```text
ai-newspaper/
│
├── dataset/
│   ├── news.csv
│   └── generated_news.csv
│
├── models/
│
├── src/
│   ├── headline_processor.py
│   ├── summarizer.py
│   ├── news_classifier.py
│   └── newspaper_generator.py
│
├── templates/
│   └── newspaper.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dhairyathakur-ai/ai-newspaper-generator.git
```

### 2. Navigate to the Project Directory

```bash
cd ai-newspaper-generator
```

### 3. Create a Virtual Environment

```bash
py -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

If dependencies are not yet listed in `requirements.txt`, install them using:

```bash
py -m pip install flask pandas torch sentencepiece transformers
```

### 6. Run the Application

```bash
py app.py
```

### 7. Open in Your Browser

Visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 How It Works

The application follows this workflow:

1. The user enters a news headline.
2. The user provides the original news article or source text.
3. Flask receives the submitted information.
4. The article is passed to the pretrained AI summarization model.
5. The model generates a concise summary.
6. The generated summary is displayed on the webpage.

### Workflow

```text
        User Input
            |
            v
      News Headline
            |
            v
      Article Text
            |
            v
      Flask Backend
            |
            v
    AI Summarization Model
            |
            v
     Generated Summary
            |
            v
      Newspaper Display
```

---

## 🔮 Future Improvements

The project is currently in its initial development stage.

Planned features include:

- [ ] Automatic news retrieval from online sources.
- [ ] Generate complete news articles from verified source material.
- [ ] Multiple news categories such as Technology, Sports, Business, and Science.
- [ ] Support for Hindi, English, and Hinglish.
- [ ] Customizable article length and writing styles.
- [ ] Professional newspaper homepage design.
- [ ] AI-powered headline suggestions.
- [ ] Duplicate news detection.
- [ ] News history and database integration.
- [ ] Download newspaper as PDF.
- [ ] News search functionality.
- [ ] Dark mode.
- [ ] Source references and fact-checking assistance.

---

## ⚠️ Important Note

The current version generates summaries from the article text supplied by the user.

It does not yet automatically retrieve live news from the internet or independently verify news claims.

The generated summaries should be checked against their original sources before publication.

---

## 👨‍💻 Developer

**Dhairya Thakur**

Computer Science Engineering Student  
Interested in Artificial Intelligence, Machine Learning, and Software Development.

### GitHub

[dhairyathakur-ai](https://github.com/dhairyathakur-ai)

### Project Repository

[AI Newspaper Generator](https://github.com/dhairyathakur-ai/ai-newspaper-generator)

---

⭐ If you find this project interesting, consider giving the repository a star!
