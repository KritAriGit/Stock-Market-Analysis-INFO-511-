# Script to fectch raw data from yahoo finance (yfinance)

import yfinance as yf
import pandas as pd

tickers = ['NVDA', 'AAPL', 'TSLA', 'JPM', 'GS']                 # tickers  = symbols for stocks
start_date = '2020-01-01'                                       
end_date = '2025-01-01'      


