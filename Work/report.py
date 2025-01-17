# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        indices = [headers.index(colname) for colname in select]

        row = next(rows)

        for row in rows:
            try:
                record = {colname:row[index] for colname, index in zip(select, indices)}
                portfolio.append(record)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio


def read_prices(filename) -> dict:
    '''
    Reads given file for name and share price
    '''

    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                print("Couldn't parse", row)

    return prices

def make_report(portfolio, prices) -> list:
    '''
    Calculates change in share price and prints output report with Name, no.of shares, price and change
    '''
    for row in portfolio:
        try:
            change = prices[row['name']] - float(row['price'])
            row['price'] = float(prices[row['name']])
            row['change'] = change
        except:
            print('Cound not execute')

    return portfolio


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Prints report of name, shares, price and change in price of given stock portfolio file and latest price file
    '''

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}')
    print('---------- ---------- ---------- ---------- ')
    for row in report:
        price = '${:.2f}'.format(row['price'])
        print(f'{row['name']:>10s}{row['shares']:>10s}{price:>10}{row['change']:>10.2f}')
