from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentiment_analysis.finbert_model import SentimentAnalyzer  # FinBERT
from sentiment_analysis.crypto_sentiment import CryptoSentimentAnalyzer  # CryptoBERT

# Initialize FastAPI app
app = FastAPI()

# Load both sentiment analysis models
finbert_analyzer = SentimentAnalyzer()
cryptoBERT_analyzer = CryptoSentimentAnalyzer()

# Define input schema
class SentimentRequest(BaseModel):
    text: str

# API endpoint for sentiment analysis using both models
@app.post("/compare-predict")
def compare_sentiment(request: SentimentRequest):
    try:
        finbert_result = finbert_analyzer.analyze(request.text)
        crypto_result = cryptoBERT_analyzer.analyze(request.text)

        return {
            "finbert": {"label": finbert_result["label"], "score": finbert_result["score"]},
            "cryptoBERT": {"label": crypto_result["label"], "score": crypto_result["score"]}
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running"}
