import os
import re
import csv
import pandas as pd


def build_csv(walk_path, write_file):
    path_lst = []
    errors = []
    for filename in os.listdir(walk_path):
        if filename.endswith(".rtf"):
            path_lst.append(os.path.join(walk_path, filename))
    for path in path_lst:
        lable = os.path.splitext(os.path.basename(path))[0]
        with open(path, 'r') as f1:
            f1_line = f1.read()
            m = re.match(".*f1(.*)\}\r\n", f1_line, re.DOTALL)
        with open(write_file, 'a') as f2:
            writer = csv.writer(f2)
            if m is not None:
                writer.writerow((lable, m.groups()[0]))
            else:
                m = re.match(".*f0(.*)\}\r\n", f1_line, re.DOTALL)
                if m is not None:
                    writer.writerow((lable, m.groups()[0]))
                else:
                    m = re.match(".*cf0(.*)\}\n", f1_line, re.DOTALL)
                    if m is not None:
                        writer.writerow((lable, m.groups()[0]))
                    else:
                        errors.append(path)
    print "%s files successfully loaded into %s." % (len(path_lst),
                                                     os.path.basename(
                                                     write_file))
    print "%s files failed to load." % (len(errors))
    df = pd.read_csv(write_file, header=None)
    print "Sample header of %s:" % (os.path.basename(write_file))
    print df.head(5)



if __name__ == '__main__':
    build_csv('../data/ut_transcriptions_rtf',
              '../data/analysis_base_tables/ut_transcriptions.csv')
