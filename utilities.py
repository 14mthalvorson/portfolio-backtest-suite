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


def calculate_backtest_performance(cache, portfolio, settings):

    rebalancing_frequency = settings.get('rebalancing_frequency', 0.25)

    for ticker in portfolio.keys():
        lookup_price_history(cache, ticker)

    latest_start_date = 0

    for ticker in portfolio.keys():
        start_date = min(list(cache[ticker].keys()))
        latest_start_date = max(latest_start_date, start_date)

    print("Backtest Start Date:", latest_start_date)

    if latest_start_date == 0:
        print("Error with start dates")
        exit(0)

    # Portfolio Math
    cumulative_return = 1
    results = {latest_start_date: cumulative_return}
    time = round(latest_start_date + rebalancing_frequency, 2)
    today = 2023.4

    while time <= today:
        change = 0
        for ticker in portfolio.keys():
            a = get_price(cache[ticker], time - rebalancing_frequency)
            b = get_price(cache[ticker], time)
            if a is None or b is None:
                print("None result", cache[ticker], time - rebalancing_frequency, time)
                exit(0)
            weight = portfolio[ticker] / 100
            change += weight * (b / a - 1)

        cumulative_return *= change + 1
        results[time] = cumulative_return
        time = round(time + rebalancing_frequency, 2)

    # Analysis - Portfolio Metrics
    cagr = cumulative_return ** (1 / (today - latest_start_date))
    print('CAGR: {:.2%}'.format(cagr - 1))

    return results