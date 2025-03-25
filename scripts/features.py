
# ------------------------- Feature Engineering -------------------------
# This script should read raw stock data, process it to calculate daily returns, moving averages (30 & 100), and 30-day volatility, 
# and saves the processed datasets to the processed folder.
# if not then           sad....      - KS



import pandas as pd
import os

# Symbols and paths

tickers = ['NVDA', 'AAPL', 'TSLA', 'JPM', 'GS']
raw_data_path = "data/raw data/"
pro_data_path = "data/processed data/"

os.makedirs( pro_data_path, exist_ok = True )

# Feature Engineering

def process_stock_data(ticker):

    file_path = os.path.join( raw_data_path, f"{ticker}_stock_data.csv" )

    df = pd.read_csv(file_path, skiprows=2)
    df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    df['Date'] = pd.to_datetime( df['Date'] )
    df.set_index( 'Date', inplace = True )

    # Daily Returns

    df['Daily Return'] = df['Close'].pct_change()

    # Moving Averages

    df['MA_30'] = df['Close'].rolling( window = 30 ).mean()
    df['MA_100'] = df['Close'].rolling( window = 100 ).mean()

    # 30-day Rolling Volatility                                                     (standard deviation of returns)

    df['Volatility_30'] = df['Daily Return'].rolling(window = 30).std()

    # Saving

    processed_file_path = os.path.join( pro_data_path, f"{ticker}_processed.csv" )
    df.to_csv(processed_file_path)
    print(f"processed data saved for {ticker} to {processed_file_path}")

for ticker in tickers:
    process_stock_data(ticker)

print("\nFeature engineering done.")


