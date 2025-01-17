# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of record
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')


    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        #Read the file headers if any
        if has_headers:
            headers = next(rows)

            #If a column selector was given, find the indices of the specified columns
            #Also narrow the set of headers used for the resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
        else:
            headers = []

        records = []

        for rowno, row in enumerate(rows, 1):
            if not row: #Skip rows with no data
                continue

            #If specific column indices are selected pick them
            if select:
                row = [row[index] for index in indices]

            #Data type conversion if specified
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            # Make a dictionary
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records
