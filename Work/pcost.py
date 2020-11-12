# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    totalCost = 0.0
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)

            for row in rows:
                totalCost += float(row[2]) * int(row[1])   
        return totalCost
    except ValueError:
        raise RuntimeError('Invalid file path. Please check you entered a correct path.')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
print(f"Total cost: {portfolio_cost(filename)}")