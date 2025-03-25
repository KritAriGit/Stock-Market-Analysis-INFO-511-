#libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

tickers = ['NVDA', 'AAPL', 'TSLA', 'JPM', 'GS']                                                 #again - tickers = symbols for stocks
raw_data_path = "data/raw data/"

# Load stock data
stocks = {}
for x in tickers:
    file_path = os.path.join(raw_data_path, f"{x}_stock_data.csv")

    if os.path.exists(file_path):
        df = pd.read_csv(file_path, skiprows = 2)                                               # Skipping first two rows, due to csv structure
        
        # Renaming columns
        df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
        df['Date'] = pd.to_datetime(df['Date'])                                                 # Converting Date to datetime
        df.set_index('Date', inplace = True)                                                    # Setting Date as index
        
        stocks[x] = df
        print(f"Data loaded successfully for {x}")
    else:
        print(f"Data file is missing for {x}: {file_path}")

# # ------------ Just for Verification ignore this part ----------------

# print(stocks['AAPL'].head())

# Exploratory Data Analysis (EDA)

# for x, df in stocks.items():
#     print(f"\nEDA for {x} : \n")
#     print(df.describe())  
#     print(df.info())  
#     print(f"Missing values :\n{df.isnull().sum()}")

# ------------------------------------------------------------------------

# Plot stock price trends

plt.figure(figsize = (12, 6))

for x, df in stocks.items():
    plt.plot(df.index, df['Close'], label = x)

plt.legend()
plt.title("Stock Price Trends (Close)")
plt.xlabel("Year")
plt.ylabel("Close Price")
plt.grid()
plt.show()

# to check missing values visually

plt.figure(figsize=(12, 6))
sns.heatmap(pd.concat({ticker: df.isnull().sum() for ticker, df in stocks.items()}, axis=1), annot=True, cmap = 'coolwarm', cbar = True)
plt.title("Missing Data Heatmap for All Stocks")
plt.show()
