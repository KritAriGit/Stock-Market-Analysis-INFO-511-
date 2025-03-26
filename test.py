# file to test codes / functions / methods 



import pandas as pd
import matplotlib.pyplot as plt
import os

# Define tickers by sector
tickers_tech = ['NVDA', 'AAPL', 'TSLA']
tickers_finance = ['JPM', 'GS']
processed_path = "data/processed/"

# Load processed stock data
def load_processed_data(ticker):
    file_path = os.path.join(processed_path, f"{ticker}_processed.csv")
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    df['Cumulative Return'] = (1 + df['Daily Return']).cumprod()
    return df

# Collect data
data = {}
for ticker in tickers_tech + tickers_finance:
    data[ticker] = load_processed_data(ticker)

# Plot cumulative returns comparison
plt.figure(figsize=(14, 7))
for ticker in tickers_tech:
    plt.plot(data[ticker].index, data[ticker]['Cumulative Return'], label=f"{ticker} (Tech)")
for ticker in tickers_finance:
    plt.plot(data[ticker].index, data[ticker]['Cumulative Return'], label=f"{ticker} (Finance)")

plt.title("Cumulative Returns: Tech vs Finance Stocks (2020-2024)")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate and print average volatility per sector
print("\nAverage 30-Day Rolling Volatility (Post-COVID):")
print("Tech Sector:")
for ticker in tickers_tech:
    avg_vol = data[ticker]['Volatility_30'].mean()
    print(f"  {ticker}: {avg_vol:.4f}")

print("\nFinance Sector:")
for ticker in tickers_finance:
    avg_vol = data[ticker]['Volatility_30'].mean()
    print(f"  {ticker}: {avg_vol:.4f}")
