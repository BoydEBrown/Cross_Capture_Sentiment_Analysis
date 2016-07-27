'''
1. Sort csvs by data frame shape.
2. Select individaual colums, rows.
3. Append relevent colums, rows to master csv.
'''

import pandas as pd
import os

master_csv =
def make_master_txt_csv(csv_dir, master_csv):

def sort(csv_dir):
    shapes = []
    d = {}

    for csv in os.listdir(csv_dir):
        df = pd.read_csv(csv_dir + csv)
        shapes.append((df.shape, csv))

    for key, value in shapes:
        if key not in d:
            d[key] = []
        d[key].append(value)
    return d

def select():
    for k, v in d.iteritems():
        if k == (104, 11):
            pass
            

def append_to_master():
    pass

if __name__ == '__main__':
    main()
