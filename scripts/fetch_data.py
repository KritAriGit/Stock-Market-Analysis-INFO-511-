# ------------- Script to fectch raw data from yahoo finance (yfinance) -------------------

import yfinance as yf
import pandas as pd

tickers = ['NVDA', 'AAPL', 'TSLA', 'JPM', 'GS']                 # tickers  = symbols for stocks
startD = '2020-01-01'                                       
endD = '2025-01-01'      

def get_stock(x):
    print(f"Fetching for {x}...")
    data = yf.download(x, start = startD, end = endD)
    file_path = f"data/raw data/{x}_stock_data.csv"
    data.to_csv(file_path)
    print(f"Saved to {file_path}")

# Fetch data for all tickers
for ticker in tickers:
    get_stock(ticker)

print("Data has been successfully fetched.")

