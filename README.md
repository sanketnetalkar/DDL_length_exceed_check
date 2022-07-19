# DDL_length_exceed_check

The Python script iterates through each record in every column of the csv file. and checks whether if the record is crossing the set ddl limit (In the DB schema). As a output the code gives us the index and the records which exceed the ddl limit. By doing this, at a single glance we know which record is crossing the ddl limit instead of checking for all the records manually. 

The python script is written using two popular python modules:
1. Pandas
2. Polars

comparatively polars is 4X faster than pandas. 
I will provide both the scripts, refer any one which best fits your purpose :-)
