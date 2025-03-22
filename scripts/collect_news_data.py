import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load API keys from .env
dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path=dotenv_path)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Define API URL
url = f"https://newsapi.org/v2/everything?q=cryptocurrency&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

# Make request to NewsAPI
response = requests.get(url)
news_data = response.json()

# Extract articles
articles = news_data.get("articles", [])

# Data collection
data = []
for article in articles:
    data.append({
        "source": article["source"]["name"],
        "author": article["author"],
        "title": article["title"],
        "description": article["description"],
        "url": article["url"],
        "published_at": article["publishedAt"]
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV inside data_collection/news/
output_file = "../data_collection/news/crypto_news.csv"
df.to_csv(output_file, index=False)

print(f"✅ Successfully collected {len(df)} news articles and saved to {output_file}")
