# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)

            for rowno, row in enumerate(rows, start=1):
                record = dict(zip(headers, row))
                
                try:
                    nshares = int(record['shares'])
                    price = float(record['price'])
                    total_cost += nshares * price
                    # This catches errors in int() and float() conversions above
                except ValueError:
                    print(f'Row {rowno}: Bad row: {row}')
        
        return total_cost

    except ValueError:
        raise RuntimeError('Invalid file path. Please check you entered a correct path.')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
print(f"Total cost: {portfolio_cost(filename)}")