# ticker.py

from .follow import follow
import csv
from . import report
from . import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['Name', 'Price', 'Change'])
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['Name'] in portfolio)

    #Printing it out in required format
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([ row['Name'], f"{row['Price']:0.2f}", f"{row['Change']:0.2f}"] )

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile logfile format' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
