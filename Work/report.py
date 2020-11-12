# report.py
#
# Exercise 2.4

import csv

portfolio = []

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]), 
                'price': float(row[2])
            }

            #holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        
    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
               prices[row[0]] = float(row[1])

    return prices    
        

def gain_loss(portfolio, prices):
    total_cost = 0.0
    total_value = 0.0

    for s in portfolio:
        total_cost += s['shares']*s['price']

    for s in portfolio:
        total_value += s['shares']*prices[s['name']]

    return total_value - total_cost

def single_gain_loss(share, price, current_price):
    total_cost = 0.0
    total_value = 0.0

    total_cost += share*price

    total_value += share*current_price

    return total_value - total_cost

def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        #report.append((s[0], int(s[1]), float(prices[s[0]]), single_gain_lossint(int(s[1]),float(s[2]),float(prices[s[0]]))))
        
        sname = s['name']
        sshare = s['shares']
        sprice = prices[s['name']]
        schange = sprice - s['price']
        #report.append((s['name'], s['shares']))
        report.append((sname, sshare, sprice, schange))
    return report
         
