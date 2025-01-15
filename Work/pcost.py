# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    TotalCost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                t = (row[0], int(row[1]), float(row[2]))
                name, shares, price = t
                TotalCost = TotalCost + shares*price
            except ValueError:
                print("Couldn't parse", row)
    return TotalCost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total Cost = {cost}')
