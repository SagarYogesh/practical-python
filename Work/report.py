# report.py
#
# Exercise 2.4

import csv

def make_report(portfolio, prices):
    report = portfolio

    for row in report:
        try:
            change = prices[row['name']] - float(row['price'])
            row['price'] = float(prices[row['name']])
            row['change'] = change
        except:
            print('Cound not execute')

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}')
    print('---------- ---------- ---------- ---------- ')
    for row in report:
        price = '${:.2f}'.format(row['price'])
        print(f'{row['name']:>10s}{row['shares']:>10s}{price:>10}{row['change']:>10.2f}')



def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        columns = next(rows)
        for row in rows:
            try:
                holding = dict(zip(columns, row))
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
                prices[row[0]] = float(row[1])
            except:
                print("Couldn't parse", row)

    return prices

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
make_report(portfolio, prices)
