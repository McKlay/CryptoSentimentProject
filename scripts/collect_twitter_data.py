import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Authenticate with Twitter API (Using Bearer Token for v2 API)
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

# Define search query for cryptocurrency tweets
QUERY = "Bitcoin OR Ethereum OR Crypto OR Cryptocurrency OR Blockchain -is:retweet lang:en"
TWEET_COUNT = 100  # Adjust as needed

# Fetch tweets
tweets = client.search_recent_tweets(query=QUERY, tweet_fields=["created_at", "text", "public_metrics"], max_results=TWEET_COUNT)

# Extract tweet data
data = []
for tweet in tweets.data:
    data.append({
        "timestamp": tweet.created_at,
        "text": tweet.text,
        "retweets": tweet.public_metrics["retweet_count"],
        "likes": tweet.public_metrics["like_count"]
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV inside data_collection folder
output_file = "../data_collection/twitter/crypto_tweets.csv"
df.to_csv(output_file, index=False)

print(f"✅ Successfully collected {len(df)} tweets and saved to {output_file}")
