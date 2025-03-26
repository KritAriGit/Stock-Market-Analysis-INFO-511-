import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# tickers
tech_tickers = ['NVDA', 'AAPL', 'TSLA']
fin_tickers = ['JPM', 'GS']
processed_path = "data/processed/"

# data
def load_processed_data(ticker):
    file_path = os.path.abspath(os.path.join(processed_path, f"{ticker}_processed.csv"))
    df = pd.read_csv(file_path, parse_dates = ['Date'], index_col = 'Date')
    df['Cumulative Return'] = (1 + df['Daily Return']).cumprod()
    df['Ticker'] = ticker
    return df

# combine data
all_data = pd.concat([load_processed_data(t) for t in tech_tickers + fin_tickers])
all_data['Sector'] = all_data['Ticker'].apply(lambda x: 'Tech' if x in tech_tickers else 'Finance')



# plot
sns.set_style("whitegrid")
plt.figure(figsize=(14, 7))
palette = sns.color_palette("tab10")

# different styles for tech and fin
for i, ticker in enumerate(tech_tickers + fin_tickers):
    subset = all_data[all_data['Ticker'] == ticker]
    linestyle = '-' if ticker in tech_tickers else '--'
    plt.plot(subset.index, subset['Cumulative Return'],
             label = f"{ticker} ({'Tech' if ticker in tech_tickers else 'Finance'})",
             linestyle = linestyle, linewidth = 1.5)

plt.grid(True, alpha = 0.3)

yticks = plt.yticks()[0]
plt.yticks(yticks, [f"{y:.0f}x" for y in yticks])

plt.title("Cumulative Returns: Tech vs Finance Stocks (2020–2024)", fontsize = 16)
plt.xlabel("Date", fontsize = 12)
plt.ylabel("Cumulative Return", fontsize = 12)
plt.legend()
plt.tight_layout()
plt.show()