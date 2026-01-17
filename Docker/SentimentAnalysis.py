from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

@app.get("/")
def home():
    return {"status": "Sentiment AI is Online 🧠"}

@app.get("/analyze")
def analyze_sentiment(text: str):
    # 1. Calculate the sentiment scores
    scores = analyzer.polarity_scores(text)
    compound_score = scores['compound']

    # 2. Decide the label
    label = "Neutral"
    if compound_score > 0.05:
        label = "Positive"
    elif compound_score < -0.05:
        label = "Negative"

    # 3. Return the result
    return {
        "text_received": text,
        "sentiment_label": label,
        "confidence_score": compound_score
    }