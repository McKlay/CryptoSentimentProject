# 🚀 CryptoSentimentProject

An AI-powered platform for **real-time sentiment analysis** and **price prediction** in the cryptocurrency market. This end-to-end system gathers live data from Twitter, Reddit, and financial news APIs, processes sentiment using transformer models like **FinBERT**, and forecasts crypto prices using deep learning models. Results are visualized through an interactive **ReactJS dashboard**, backed by a **FastAPI** RESTful server.

---

## 📁 Project Folder Structure

```
CryptoSentimentProject/
├── cryptoenv/                 # Virtual environment (ignored by Git)
├── data/                      # Cleaned datasets for ML and dashboards
├── data_collection/           # Scripts to gather raw data (Twitter, Reddit, News)
├── frontend/                  # ReactJS dashboard for UI
├── models/                    # Trained model weights and checkpoints
├── notebooks/                 # Jupyter notebooks for exploration and prototyping
├── prediction_model/          # Scripts for training and predicting prices
├── scripts/                   # Automation scripts (preprocessing, scheduling)
├── sentiment_analysis/        # Core sentiment pipeline logic
│   ├── finbert_model.py       # Load and run FinBERT/StockBERT models
│   ├── preprocess.py          # Text cleaning and tokenization
│   └── sentiment_utils.py     # Utilities for scoring and results formatting
├── app.py                     # FastAPI backend entry point
├── .env                       # Environment variables (API keys, secrets)
├── requirements.txt           # Python dependencies list
└── README.md                  # Project documentation
```

---

## 🛠 Technologies Used

- **Python**, **FastAPI**, **ReactJS**
- **Transformers** (FinBERT/StockBERT)
- **TensorFlow/Keras** for price prediction
- **Pandas, NumPy, NLTK** for data cleaning
- **Docker** and **GitHub Actions** (future enhancement)
- **Jupyter Notebooks** for experimentation

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/McKlay/CryptoSentimentProject.git
cd CryptoSentimentProject
```

2. **Set up the virtual environment**
```bash
python -m venv cryptoenv
source cryptoenv/bin/activate   # On Windows: cryptoenv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure your `.env` file**
```
TWITTER_API_KEY=your_key_here
REDDIT_CLIENT_ID=your_id
REDDIT_SECRET=your_secret
NEWS_API_KEY=your_key_here
```

4. **Run the backend**
```bash
uvicorn app:app --reload
```

5. **Start the frontend**
```bash
cd frontend
npm install
npm start
```

---

## 📈 API Endpoints

| Endpoint             | Method | Description                          |
|----------------------|--------|--------------------------------------|
| `/analyze_sentiment` | POST   | Analyze text sentiment               |
| `/predict_price`     | POST   | Predict future price for a token     |
| `/get_trends`        | GET    | Historical sentiment trend data      |

---

## 🙌 Author

**Clay Mark Sarte** — [LinkedIn](https://linkedin.com/in/your-profile)  
Feel free to connect and discuss AI, ML, crypto, or cool startup ideas!

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.