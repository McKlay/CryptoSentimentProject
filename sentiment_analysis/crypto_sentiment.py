from transformers import pipeline
import torch

class CryptoSentimentAnalyzer:
    def __init__(self, model_name="ElKulako/cryptobert"):
        device = 0 if torch.cuda.is_available() else -1
        self.pipeline = pipeline("sentiment-analysis", model=model_name, device=device)

    def analyze(self, text):
        result = self.pipeline(text)
        label = result[0]["label"]  # Model directly returns "Bullish", "Bearish", or "Neutral"

        # Print debug info
        print(f"DEBUG: Model output label -> {label}")

        return {"label": label, "score": result[0]["score"]}
