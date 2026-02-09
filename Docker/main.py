from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

@app.get("/")
def home():
    return {"status": "Hydra Unified API Online", "capabilities": ["ML Prediction", "Sentiment Analysis"]}

# Endpoint 1: Score Prediction
@app.get("/predict")
def predict(hours: float):
    return {
        "input_hours": hours,
        "prediction_score": hours * 10.0,
        "method": "Simulated Linear Regression"
    }

# Endpoint 2: Sentiment Analysis
@app.get("/analyze")
def analyze(text: str):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    label = "Positive" if compound > 0.05 else "Negative" if compound < -0.05 else "Neutral"
    
    return {
        "text": text,
        "sentiment": label,
        "score": compound
    }