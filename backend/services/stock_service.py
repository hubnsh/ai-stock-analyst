import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_KEY")

def get_stock_data(symbol: str):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    try:
        data = requests.get(url, params=params).json()
        q = data["Global Quote"]
        return {
            "symbol": symbol,
            "price": float(q["05. price"]),
            "change": float(q["09. change"]),
            "volume": q["06. volume"]
        }
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return {"symbol": symbol, "price": 0, "change": 0}
