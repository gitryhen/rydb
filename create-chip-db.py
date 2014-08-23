# create-chip-db.py
# version 0.3
# Henry Kelderman
# 2014-08-20
# 0.3 put file under SVN version control
# 0.2 added basic database functionality
# 0.1 initial experiments
# ideas: use tuples instead of lists for more efficient memory management.

import csv
import sqlite3


def insertintotable(connection, row):
    # FIXME exectuemany zou hier beter
    connection.execute('INSERT INTO testtab VALUES (' +
                       ', '.join(row) + ')')


if __name__ == '__main__':
    myfile = '/home/henry/test.csv'
    ##    myfile = 'C:\\Users\\Henry\\Documents\\P\\chipproduction\\Measurements_Wafer_Processing_Cleanroom_HeaderProvidedOnFirstRow.csv'
    with open(myfile) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ';')
        # read header
        # header = csvreader.__next__()
        fields = [heading.replace('-', '') for
                  heading in next(csvreader) if heading != '']
        # fields = [heading.replace('-','') for heading in header if heading != '']
        print(fields)
        # for row in csvreader:  # does not reset csv.reader
        #     print(', '.join(row))
        try:
            con = sqlite3.connect(":memory:")
            c = con.cursor()
            # Create table
            c.execute('create table testtab (' +
                      ' text, '.join(fields) + ')')
            for row in csvreader:
                insertintotable(c, [', '.join(element) for element in row])
            print('----')
            [print(row) for row in c.execute('SELECT * FROM testtab')]
            con.commit()
            con.close()
        except:
            print('Except error, closing connection to database')
            con.close()

# execute-many: https://docs.python.org/3.4/library/sqlite3.html

# # Larger example that inserts many records at a time
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
