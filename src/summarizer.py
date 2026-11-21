from transformers import pipeline

# Load pretrained summarization model
print("Loading AI Summarization Model...")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    device=-1
)

print("Model Loaded Successfully!")


def generate_summary(article):

    result = summarizer(
        article,
        max_length=80,
        min_length=10,
        do_sample=False,
        truncation=True
    )

    return result[0]["summary_text"]


if __name__ == "__main__":

    article = """
    Artificial intelligence is transforming the healthcare industry.
    Doctors are increasingly using AI-powered tools to analyze medical
    images, detect diseases and improve patient care. Researchers are
    also developing advanced systems to assist medical professionals.
    """

    summary = generate_summary(article)

    print("\nOriginal Article:")
    print(article)

    print("\nGenerated Summary:")
    print(summary)