# DDL_length_exceed_check

The Python script iterates through each record in every column of the csv file. and checks whether if the record is crossing the set ddl limit (In the DB schema). As a output the code gives us the index and the records which exceed the ddl limit. By doing this, at a single glance we know which record is crossing the ddl limit instead of checking for all the records manually. This script will be useful when you upload data to database. 

The python script is written using two popular python modules:
1. Pandas
2. Polars

The script uses argparse, which takes command line arguments. 
first argument takes the file name: -f <file_name.csv>
second argument takes a dictionary of columns and limits: -d "{'col1':limit}"
example: 
python file_name.py -f browse.csv -d "{'col1':100, 'col2':(10,6)}"


comparatively polars is 4X faster than pandas. 
I will provide both the scripts, refer any one which best fits your purpose :-)
