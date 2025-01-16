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
        headers = next(rows)
        for rownum, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                TotalCost += nshares * price
            except ValueError:
                print(f'Row {rownum}: Couldn\'t parse {row}')
    return TotalCost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total Cost = {cost}')
