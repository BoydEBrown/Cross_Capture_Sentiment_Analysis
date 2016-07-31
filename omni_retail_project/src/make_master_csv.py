'''
1. Sort csvs by data frame shape.
2. Select individaual colums, rows.
3. Append relevent colums, rows to master csv.
'''

import pandas as pd
import os


master_csv = '/Users/boydbrown/Cross_Capture_Sentiment_Analysis/ \
omni_retail_project/data/analysis_base_tables/master_text.csv'


def make_master_txt_csv(csv_dir, master_csv):
    pass

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

# If this doesn't work, rewrite select() to concatinat all non-nan
# cells in column after row x (or 33?), by column.


def select(d):  # dictionary from def sort
    for k, v in d.iteritems():
        if k == (104, 11):
            rows = [7, 8, 12, 14, 96, 98, 99, 100, 103]
        if k == (95, 11):
            rows = [7, 8, 12, 14, 87, 90, 92, 94]
        if k == (95, 7):
            rows = [7, 8, 12, 14, 87, 90, 92, 94]
        if k == (86, 11):
            rows = [7, 8, 12, 14, 79, 81, 83, 85]
        if k == (86, 8):
            rows = [7, 8, 12, 14, 78, 81, 83, 85]
        if k == (80, 11):
            rows = [7, 8, 12, 14, 72, 75, 77, 79]
        if k == (78, 11):
            rows = [7, 8, 12, 14, 70, 73, 75, 77]
        if k == (77, 11):
            rows = [7, 8, 12, 14, 68, 72, 74, 76]
        if k == (72, 11):
            rows = [7, 8, 12, 14, 64, 67, 69, 71]
        if k == (71, 11):
            rows = [7, 8, 12, 14, 63, 66, 68, 70]
        if k == (69, 11):
            rows = [7, 8, 12, 14, 61, 64, 66, 68]
        if k == (68, 11):
            rows = [7, 8, 12, 14, 60, 63, 65, 67]
        if k == (66, 11):
            rows = [7, 8, 12, 14, 58, 61, 63, 65]
        if k == (63, 11):
            rows = [7, 8, 12, 14, 55, 58, 60, 62]
        if k == (62, 21):
            rows = [7, 8, 12, 14, 54, 57, 59, 61]
        if k == (62, 11):
            rows = [7, 8, 12, 14, 54, 57, 59, 61]
    return rows


def get_questions(dataframe):
    '''Returns a list of strings from rows 36+ in column 0.'''
    quest_blob = []
    for row in dataframe.iloc[36:, 0]:
        if str(row) != 'nan':
            quest_blob.append(row)
    return "".join(str(quest_blob))


def get_answers(dataframe):
    '''Returns a list of touples, each containing column name and
    a list of strings from rows 36+ by column.'''
    ans_lst = []
    for column in enumerate(df3):
        ans = []
        for row in df2.iloc[36:, column[0]]:
            if str(row) != 'nan':
                ans.append(row)
        ans_lst.append((column[1], "".join(str(ans))))
    print ans_lst


def append_to_master():
    pass

if __name__ == '__main__':
    main()
