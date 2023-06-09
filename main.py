import matplotlib.pyplot as plt
from utilities import *


# Create a cache. In the future, this should be loading the cache?
cache = {}

# Create new portfolios
portfolios = [
    {'vfinx': 100, 'vustx': 0},
    {'vfinx': 90, 'vustx': 10},
    {'vfinx': 80, 'vustx': 20},
    {'vfinx': 70, 'vustx': 30}]

settings = {'rebalancing_frequency': 0.25}

for portfolio in portfolios:
    name = str(portfolio)
    results = calculate_backtest_performance(cache, portfolio, settings)

    # Visualization
    x = list(results.keys())
    y = list(results.values())

    plt.plot(x, y)
    plt.scatter(x, y, s=3, label="Portfolio {}".format(name))


# Set y-axis to log scale
plt.yscale('log')

plt.legend()

# Display the plot
plt.show()




