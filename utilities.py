import yfinance as yf


# Converts year string YYYY-MM-DD to year decimal YYYY.nn
def date_str_to_year_decimal(s):
    if len(s) != 10:
        print("Error with input length: '%s'" % s)
        exit(1)
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:])
    return round(y + ((m - 1) * 30.4 + d) / 365, 2)


# Tries 3 times to get a price near the intended date
def get_price(prices_dict, year_decimal):
    for i in range(6):
        adj_year_decimal = round(year_decimal + i / 100, 2)
        if adj_year_decimal in prices_dict.keys():
            return prices_dict[adj_year_decimal]
    return None


def lookup_price_history(cache, ticker):
    tickerData = yf.Ticker(ticker)
    tickerDf = tickerData.history(period='max')

    close_prices = list(tickerDf.to_dict()['Close'].items())
    ticker_prices = {}

    for date, price in close_prices:
        date_str = str(date)[:10]
        year_decimal = date_str_to_year_decimal(date_str)
        ticker_prices[year_decimal] = price

    cache[ticker] = ticker_prices
