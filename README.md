
📁 Project Folder Structure
CryptoSentimentProject/
│
├── cryptoenv/                 
├── data/                      
├── data_collection/           
├── frontend/                  
├── models/                    
├── notebooks/                 
├── prediction_model/          
├── scripts/                   
├── sentiment_analysis/        
│   ├── finbert_model.py       
│   ├── preprocess.py          
│   └── sentiment_utils.py     
├── app.py                     
├── .env                       
├── requirements.txt           
└── README.md  

🔹 cryptoenv/
Contains the virtual environment configuration. This directory holds all Python environment dependencies and packages installed in isolation for this project.

🔹 data/
Stores processed datasets used for training and inference. This includes cleaned, structured, and final datasets ready for machine learning workflows and dashboards.

🔹 data_collection/
Contains scripts and files for gathering raw data from various sources such as Twitter, Reddit, and financial news outlets. It serves as the staging area for unprocessed, real-time data used in analysis and model training.

🔹 frontend/
Houses the ReactJS-based dashboard for visualizing real-time sentiment analysis and market predictions. This is the UI layer that communicates with the FastAPI backend via RESTful APIs.

🔹 models/
Contains trained model artifacts, weights, and checkpoint files. These are the outputs of model training sessions and are used for inference during predictions.

🔹 notebooks/
Includes Jupyter notebooks used for data exploration, visualization, experimentation, and prototyping machine learning models. Ideal for testing out features before integrating them into production scripts.

🔹 prediction_model/
Contains Python scripts that define and manage the deep learning architecture used for stock or crypto price prediction. These scripts are modularized for easy training, testing, and deployment.

🔹 scripts/
Includes automation scripts for data ingestion, data cleaning, preprocessing, scheduling tasks, or other workflow utilities. This is where reusable or scheduled processing logic resides.

🔹 sentiment_analysis/
This directory holds the core logic for the sentiment analysis pipeline. It integrates pre-trained models (like FinBERT or StockBERT) and text processing utilities for analyzing sentiment from textual data.

finbert_model.py: Handles loading and inference using FinBERT or similar transformer-based sentiment models.
preprocess.py: Provides text cleaning, tokenization, and normalization functions required before passing text to sentiment models.
sentiment_utils.py: Contains helper functions for scoring, formatting, and evaluating sentiment outputs.
🔹 app.py
The main FastAPI backend entry point. It exposes APIs for sentiment analysis and prediction functionalities, connecting the machine learning models to the frontend or any external service.

🔹 .env
A secure file used to store environment variables such as API keys, database URIs, and secret credentials. Not to be tracked by version control.

🔹 requirements.txt
Lists all the required Python libraries and packages needed to run the project. This file can be used to set up the environment via pip install -r requirements.txt.

🔹 README.md
You’re reading it! This file provides a comprehensive overview of the project, setup instructions, usage guidelines, and folder structure documentation.


