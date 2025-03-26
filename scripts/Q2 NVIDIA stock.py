import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use( 'dark_background' )
sns.set_style( "white" )

# dates and labels

event_dates = {
    "2020-09-01": "RTX 30 Launch",
    "2022-09-20": "RTX 40 Reveal",
    "2023-03-21": "GTC 2023",
    "2024-01-08": "CES 2024",
    "2024-08-23": "New AI Platform"
}

# data

processed_path = "data/processed/"
ticker = "NVDA"
file_path = os.path.abspath( os.path.join( processed_path, f"{ticker}_processed.csv" ) )
df_nvda = pd.read_csv( file_path, parse_dates=['Date'], index_col='Date' )
df_nvda['Cumulative Return'] = ( 1 + df_nvda['Daily Return'] ).cumprod( )

# Plot

fig, ax = plt.subplots( figsize=( 14, 7 ) )
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.plot( df_nvda.index, df_nvda['Close'], color = "#76B900", linewidth = 2 )                           # ( NVIDIA green: #76B900 ) Source : https://www.brandcolorcode.com/nvidia

# events
for date_str, label in event_dates.items():

    event_date = pd.to_datetime(date_str)

    if event_date in df_nvda.index:
        ax.axvline( event_date, color = 'white', linestyle = '--', alpha = 0.5 )
        ax.text( event_date, df_nvda['Close'].max()*0.95, label, rotation = 90,
                verticalalignment = 'top', horizontalalignment = 'right', fontsize = 9, color = 'white' )

# Labels and formatting
ax.set_title( "NVIDIA Stock Price with Major Product Launches ( 2020–2024 )", fontsize = 16, color = 'white' )
ax.set_xlabel( "Date", fontsize = 12, color = 'white' )
ax.set_ylabel( "Stock Price ( USD )", fontsize = 12, color = 'white' )
ax.tick_params( colors = 'white' )
ax.grid( True, alpha = 0.3)
plt.show()
