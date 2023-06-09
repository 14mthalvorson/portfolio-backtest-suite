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


# Create new portfolios
portfolio = {'vfinx': 70, 'vustx': 30}

for ticker in portfolio.keys():
    lookup_price_history(ticker)

latest_start_date = 0

for ticker in portfolio.keys():
    start_date = min(list(cache[ticker].keys()))
    print(start_date)
    earliest_start_date = max(latest_start_date, start_date)

print(latest_start_date)

if latest_start_date == 0:
    print("Error with start dates")
    exit(0)

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

