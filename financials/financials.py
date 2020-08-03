# pylint: disable=missing-docstring

from math import e

# TODO: 1st exercise: Define the `forward_price` function
def forward_price(spot, interest_rate, time):
    x = round(spot * (e ** (interest_rate * time)),2)

    print(x)
    return x


forward_price(100, 0.02, 1)
    
    


# TODO: 2nd exercise: Define the `short_pnl` function

def short_pnl(positions, mtm):
   y = (positions[0] - mtm[0]) + (positions[1] - mtm[1]) + (positions[2]-mtm[2])        
   return y 
    