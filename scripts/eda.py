#libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

tickers = ['NVDA', 'AAPL', 'TSLA', 'JPM', 'GS']             #tickers = symbols for stocks
raw_data_path = "data/raw data/"

#stock data
stocks = {}
for x in tickers:
    file_path = os.path.join(raw_data_path, f"{x}_stock_data.csv")
    if os.path.exists(file_path):
        stocks[x] = pd.read_csv(file_path, parse_dates = ['Date'], index_col = 'Date')
        print(f"Data loaded for {x}")
    else:
        print(f"Data file is missing for {x}: {file_path}")

# Exploratory Data Analysis (EDA)

for x, df in stocks.items():
    print(f"\nEDA for {x}:")
    print(df.describe())  # Summary statistics
    print(df.info())  # Data types and missing values
    print(f"Missing values :\n{df.isnull().sum()}")

# Plot stock price trends

plt.figure(figsize=(12, 6))

for ticker, df in stocks.items():
    plt.plot(df.index, df['Adj Close'], label=ticker)

plt.legend()
plt.title("Stock Price Trends (Adj Close)")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.grid()
plt.show()

# to chech missing values visually
missing_values = {ticker: df.isnull().sum().sum() for ticker, df in stocks.items()}
print("Total Missing Values:", missing_values)

sns.heatmap(pd.DataFrame(missing_values, index = ["Missing Values"]), annot = True, cmap='coolwarm')
plt.title("Missing Data Heatmap")
plt.show()
