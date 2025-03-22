import os
import pandas as pd
import re

def clean_text(text):
    """Standardizes text by removing URLs, special characters, and extra spaces."""
    text = str(text).lower()  # Convert to lowercase
    text = re.sub(r'http\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions (@username)
    text = re.sub(r'#\w+', '', text)  # Remove hashtags
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    text = text.strip()  # Remove extra spaces
    return text

# Define a simple stopword list
stopwords_list = set([
    "a", "an", "and", "are", "as", "at", "be", "but", "by",
    "for", "if", "in", "into", "is", "it", "no", "not", "of",
    "on", "or", "such", "that", "the", "their", "then", "there",
    "these", "they", "this", "to", "was", "will", "with"
])

def remove_stopwords(text):
    """Removes stopwords from tokenized text."""
    words = text.split()
    words = [word for word in words if word not in stopwords_list]
    return " ".join(words)

def preprocess_file(file_path, text_column):
    """Preprocesses a CSV file by cleaning and filtering text data."""
    df = pd.read_csv(file_path)
    
    # Remove duplicates
    df = df.drop_duplicates(subset=[text_column])
    
    # Remove missing values in text column
    df = df.dropna(subset=[text_column])
    
    # Apply text cleaning
    df['cleaned_text'] = df[text_column].apply(clean_text)
    
    # Apply stopword removal
    df['processed_text'] = df['cleaned_text'].apply(remove_stopwords)
    
    return df

def main():
    # 1. Get the absolute path to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Get the project root (one level above 'scripts')
    project_root = os.path.dirname(script_dir)
    
    # 3. Build the absolute paths for data_collection and the processed folder
    data_collection_dir = os.path.join(project_root, "data_collection")
    processed_folder = os.path.join(project_root, "data", "processed")
    os.makedirs(processed_folder, exist_ok=True)
    
    # 4. Map the input files (absolute paths) to their text column names
    datasets = {
        os.path.join(data_collection_dir, "twitter", "crypto_tweets.csv"): "text",
        os.path.join(data_collection_dir, "reddit", "crypto_reddit_posts.csv"): "title",
        os.path.join(data_collection_dir, "news", "crypto_news.csv"): "description"
    }
    
    # 5. Process each file
    for file_path, text_column in datasets.items():
        if os.path.exists(file_path):
            print(f"Processing {file_path}...")
            processed_df = preprocess_file(file_path, text_column)
            
            # Save cleaned data using the original filename prefixed with 'cleaned_'
            filename = os.path.basename(file_path)
            save_path = os.path.join(processed_folder, f"cleaned_{filename}")
            processed_df.to_csv(save_path, index=False)
            print(f"Saved cleaned file: {save_path}")
        else:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
