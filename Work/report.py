# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                holding = {
                  'name':row[0],
                  'shares':int(row[1]),
                  'price':float(row[2])
                  }
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                print(row)
                prices[row[0]] = float(row[1])
            except:
                print("Couldn't parse", row)

    return prices
