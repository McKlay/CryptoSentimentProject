import praw
import pandas as pd
import os
from dotenv import load_dotenv

# Load API keys from .env
dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path=dotenv_path)

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# Define target subreddits
subreddits = ["cryptocurrency", "bitcoin", "ethereum"]

# Number of posts to retrieve
POST_LIMIT = 100

# Data collection
data = []
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.hot(limit=POST_LIMIT):
        data.append({
            "subreddit": subreddit_name,
            "title": post.title,
            "score": post.score,
            "num_comments": post.num_comments,
            "url": post.url,
            "created_utc": post.created_utc
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV inside data_collection/reddit/
output_file = "../data_collection/reddit/crypto_reddit_posts.csv"
df.to_csv(output_file, index=False)

print(f"✅ Successfully collected {len(df)} Reddit posts and saved to {output_file}")
