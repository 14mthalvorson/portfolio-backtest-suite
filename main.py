import matplotlib.pyplot as plt
import yfinance as yf
from time_utilities import *


# Collect Data and Add to Cache

cache = {}

tickerSymbol = 'qqq'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='max')

close_prices = list(tickerDf.to_dict()['Close'].items())
ticker_prices = {}

for date, price in close_prices:
    date_str = str(date)[:10]
    year_decimal = date_str_to_year_decimal(date_str)
    ticker_prices[year_decimal] = price

x = list(ticker_prices.keys())
y = list(ticker_prices.values())

plt.scatter(x, y)

plt.yscale('log')

plt.show()

