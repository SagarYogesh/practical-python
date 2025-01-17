# pcost.py
#
# Exercise 1.27

import sys
from report import read_portfolio

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = read_portfolio(filename)

    return sum([row['shares']*row['price'] for row in portfolio])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total Cost = {cost}')

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile' % args[0])
    portfolio_cost(args[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)
