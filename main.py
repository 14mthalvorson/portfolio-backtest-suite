import matplotlib.pyplot as plt
from utilities import *


# Create a cache. In the future, this should be loading the cache?
cache = {}

# Create new portfolios
portfolios = [
    {'tqqq': 32, 'cure': 21, 'lbay': 5, 'vpu': 4, 'vdc': 3, 'v': 1, 'amzn': 1.5, 'coin': 0.5, 'kmlm': 4.5, 'dbmf': 4.5, 'tmf': 4, 'edv': 4, 'btal': 14, 'vixm': 1},
    {'tqqq': 32, 'cure': 21, 'vpu': 6, 'vdc': 6, 'v': 1, 'amzn': 2, 'fut': 4.5, 'wtmf': 4.5, 'tmf': 4, 'edv': 4, 'btal': 14, 'vixm': 1}]

settings = {'rebalancing_frequency': 0.25}

for i, portfolio in enumerate(portfolios):
    name = "Portfolio " + str(i + 1) + ": " + clean_name(str(portfolio))
    results = calculate_backtest_performance(cache, portfolio, settings)

    # Visualization
    x = list(results.keys())
    y = list(results.values())

    plt.plot(x, y)
    plt.scatter(x, y, s=3, label=name)


# Set y-axis to log scale
plt.yscale('log')

plt.legend()

# Display the plot
plt.show()




