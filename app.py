from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    df.sort_index(inplace=True)
    df['MA_30'] = df['Close'].rolling(window=30).mean()
    df['MA_100'] = df['Close'].rolling(window=100).mean()
    df['Volatility_30'] = df['Close'].rolling(window=30).std()
    df['Daily Return'] = df['Close'].pct_change()
    df['High-Low Spread'] = df['High'] - df['Low']
    df.dropna(inplace=True)
    return df

@app.route('/')
def index():
    file_path = r"C:\Users\ual-laptop\Desktop\pro\Stock-Market-Analysis-INFO-511-\data\raw data\NVDA_stock_data.csv"
    df = load_and_preprocess_data(file_path)

    # Plot 1: Close vs Moving Averages
    fig_ma = px.line(df, x=df.index, y=['Close', 'MA_30', 'MA_100'],
                     title="Close Price vs Moving Averages")

    # Plot 2: 30-Day Rolling Volatility
    fig_volatility = px.line(df, x=df.index, y='Volatility_30',
                             title="30-Day Rolling Volatility")

    # Plot 3: Daily Return Over Time
    fig_return = px.line(df, x=df.index, y='Daily Return',
                         title="Daily Return Over Time")

    # Plot 4: Volume vs Close Price
    fig_volume = px.scatter(df, x='Volume', y='Close',
                            title="Volume vs Close Price")

    # Plot 5: High-Low Spread Over Time
    fig_spread = px.line(df, x=df.index, y='High-Low Spread',
                         title="High-Low Spread Over Time")

    # Plot 6: Histogram of Daily Returns
    fig_hist = px.histogram(df, x='Daily Return', nbins=50,
                            title="Histogram of Daily Returns")

    return render_template('index.html',
                           graph_ma=fig_ma.to_html(full_html=False),
                           graph_volatility=fig_volatility.to_html(full_html=False),
                           graph_return=fig_return.to_html(full_html=False),
                           graph_volume=fig_volume.to_html(full_html=False),
                           graph_spread=fig_spread.to_html(full_html=False),
                           graph_hist=fig_hist.to_html(full_html=False))

if __name__ == '__main__':
    app.run(debug=True)
