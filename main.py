import time
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'QQQ'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='max')

# See your data
print(tickerDf.to_dict().keys())

closes = []

print(len(tickerDf.to_dict()['Close']))

print(list(tickerDf.to_dict()['Close'].keys())[0])

date_time = str(list(tickerDf.to_dict()['Close'].keys())[0])[:10]
pattern = '%Y-%m-%d'
epoch = int(time.mktime(time.strptime(date_time, pattern)))
print(epoch)


exit(0)

for day in tickerDf.to_dict()['Close']:
    closes.append((day[0], day[1]))

print(closes[0])

# closes.sort(key=lambda x: x[0])
