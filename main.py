import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import yfinance as yf

from time_utilities import *


def lookup_price_history(ticker):
    tickerData = yf.Ticker(ticker)
    tickerDf = tickerData.history(period='max')

    close_prices = list(tickerDf.to_dict()['Close'].items())
    ticker_prices = {}

    for date, price in close_prices:
        date_str = str(date)[:10]
        year_decimal = date_str_to_year_decimal(date_str)
        ticker_prices[year_decimal] = price

    cache[ticker] = ticker_prices


# Collect Data and Add to Cache
cache = {}
tickers = ['vfinx', 'vustx']

for ticker in tickers:
    lookup_price_history(ticker)

exit(0)

# Create new portfolios

portfolio = {'vfinx': 70, 'vustx': 30}

earliest_start_date = 2024

for ticker in portfolio.keys():
    start_date = min(list(cache))



# Visualization

for ticker in tickers:
    x = list(cache[ticker].keys())
    y = list(cache[ticker].values())

    # Create scatter plot with smaller dots
    plt.scatter(x, y, s=1, label=ticker)

# Set y-axis to log scale
plt.yscale('log')

plt.legend()

# Display the plot
plt.show()

