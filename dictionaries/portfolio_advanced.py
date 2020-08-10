# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "FB": {
    "volume": 18,
    "strike": 209.0
  }
}

print(portfolio["TSLA"]["volume"])
print(portfolio["GOOG"]["strike"])

market = {
  "AAPL":  198.84,
  "GOOG": 1217.93,
  "TSLA":  267.66,
  "FB":    179.06
}


# The idea is to iterate over the real_time_market list and extract information to build the market dictionary:
    
market = {}

for stock in real_time_market:
    market[stock['symbol']] = stock['price']
    
market = dict((stock['symbol'], stock['price']) for stock in real_time_market)

symbols = ",".join(portfolio.keys())
url = f"https://api.iextrading.com/1.0/tops/last?symbols={symbols}"
real_time_market = requests.get(url).json()

