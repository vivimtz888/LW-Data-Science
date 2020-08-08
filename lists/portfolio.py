# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]

fb_stocks_count = portfolio[3][0]

#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]


def pnl(portfolio, market):        
    a = (portfolio[0][0] * market[0]) - (portfolio[0][0] * portfolio[0][1]) 
    g = (portfolio[1][0] * market[1]) - (portfolio[1][0] * portfolio[1][1])
    t = (portfolio[2][0] * market[2]) - (portfolio[2][0] *portfolio[2][1])
    f = (portfolio[3][0] * market[3]) - (portfolio[3][0] *portfolio[3][1])
    tot = a + g + t + f
    print(tot) 
    
    

    
new_pnl = pnl(portfolio, market)


 