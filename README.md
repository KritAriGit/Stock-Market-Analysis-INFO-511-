Stock Market Analysis: Post-COVID Trends & NVIDIA Event Impact

📌 Overview

This project focuses on the aspects of Data Management and Visualisation in Data Science, diving into the stock trends of Tech and Finance giants (i.e. companies / corporations).

👔 Team Members

o Kritvirya Singh - @KritAriGit
o Mokshagna Gnana Teja Talapaneni - (update gitid)
o Akhila Myaka - (update gitid)

🎯 Research Questions

How did tech stocks perform post-COVID compared to other sectors?

What was the impact on NVIDIA’s stock prices before and after major product launches?

📊 Selected Stocks

Technology Sectors: NVIDIA (NVDA), Apple (AAPL), Tesla (TSLA)

Finance Sector: JPMorgan Chase (JPM), Goldman Sachs (GS)

📂 Project Structure

stock-market-analysis/
├── data/
│   ├── raw/         # Raw stock data CSVs
│   ├── processed/   # Cleaned & transformed data
├── notebooks/       # Jupyter notebooks for analysis
├── scripts/         # Data fetching & processing scripts
├── README.md        # Project documentation

🔍 Methods & Approach

Source of the data : Yahoo Finance API (via yfinance Python library)

Data Collection: Stock price data (2020 - present)

Data Processing: Handling missing values, stock splits, daily returns, and moving averages          # in progress

Analysis Techniques: Time-series analysis, volatility comparisons, and event-driven stock behavior  # (need to confirm)

Visualization: Matplotlib & Seaborn for trend analysis

🚀 Getting Started

🔹 Install Dependencies

pip install yfinance pandas numpy matplotlib seaborn

🔹 Fetch Stock Data

Run the provided script in the /scripts/ directory to retrieve stock data.

python scripts/data_fetcher.py

🔹 Explore Data

Open Jupyter notebooks in the /notebooks/ directory to analyze and visualize trends.

📜 License

This project makes use of the data from Yahoo finance, which is publicaly available and furthurmore does not require any special permissions.


📅 Last Updated: [Date]🔗 Project Status: In Progress