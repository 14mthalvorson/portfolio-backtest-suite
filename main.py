import matplotlib.pyplot as plt
from utilities import *


# Create a cache. In the future, this should be loading the cache?
cache = {}

# Create new portfolios
portfolios = [{'vfinx': 70, 'vustx': 30}]
rebalancing_frequency = 0.25

portfolio = portfolios[0]

def calculate_backtest_performance(portfolio):
    for ticker in portfolio.keys():
        lookup_price_history(cache, ticker)

    latest_start_date = 0

    for ticker in portfolio.keys():
        start_date = min(list(cache[ticker].keys()))
        latest_start_date = max(latest_start_date, start_date)

    print(latest_start_date)

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

results = calculate_backtest_performance(portfolio)

# Visualization
x = list(results.keys())
y = list(results.values())

plt.plot(x, y)
plt.scatter(x, y, s=3, label="Portfolio 1")


# Set y-axis to log scale
plt.yscale('log')

plt.legend()

# Display the plot
plt.show()




