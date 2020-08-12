# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

import requests

#       vol  strike
aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

variables = [ aapl, goog, tsla, fb ]
names = [ 'aapl', 'goog', 'tsla', 'fb']

portfolio = {}

#don't use for loop to create dictionaries

for i in range(4):
    portfolio[names[i]] = {'volume': variables[i][0]}
    portfolio[names[i]] = {'volume': variables[i][1]}






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

# P&L Computation

pnl = {}
total_pnl = 0

for company in portfolio:
    markup = market[company] - portfolio[company]['strike']
    pnl[company] = portfolio[company]['volume'] * markup
    total_pnl += pnl[company]
    
# optional

url = "https://api.iextrading.com/1.0/tops/last?symbols=AAPL,GOOG,TSLA,FB"
real_time_market = requests.get(url).json()

print(real_time_market)
type(real_time_market)
real_time_market[0]
real_time_market[0].keys()

api_market = dict((stock['symbol'], stock['price']) for stock in real_time_market)

print(api_market)

symbols = ",".join(portfolio.keys())
url = "https://api.iextrading.com/1.0/tops/last?symbols={symbols}"
real_time_market = requests.get(url).json()


    




