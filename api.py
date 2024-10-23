"""
 API interaction module (for external data)
"""
import requests
import yfinance as yf


def get_stock_price(symbol):
    # response = requests.get(f"https://api.example.com/stock/{symbol}")
    # if response.status_code == 200:
    #     return response.json().get("price")
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")["Close"].iloc[-1]  # Get the last closing price
    if price:
        return price
    else:
        return None