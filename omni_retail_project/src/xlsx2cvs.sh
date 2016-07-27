'''Convert all .xlsx files in current directory to .csv with xlsx2csv'''


#!/bin/bash

for i in *.xlsx;
do
    filename=$(basename "$i" .xlsx);
    outext=".csv"
    xlsx2csv $i $filename$outext
done
