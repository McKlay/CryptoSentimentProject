from transformers import pipeline
import torch

class SentimentAnalyzer:
    def __init__(self, model_name="ProsusAI/finbert"):
        device = 0 if torch.cuda.is_available() else -1
        self.pipeline = pipeline("sentiment-analysis", model=model_name, device=device)

    def analyze(self, text):
        result = self.pipeline(text)
        return {"label": result[0]["label"], "score": result[0]["score"]}
