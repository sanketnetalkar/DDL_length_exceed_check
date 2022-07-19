import polars as pl
import argparse
from datetime import datetime


def ddl_limit_varchar_handle(row, limit):
    if len(str(row)) > limit:
        return 'Not Okay'
    else:
        return 'Okay'


def ddl_limit_float_handle(row, x, y):
    row = str(row)
    row_split = row.split(".")
    k = len(row_split[0]) + len(row_split[-1])
    # print(k,type(k))
    # print(x,type(x))
    # print(y,type(y))
    if (k > x) or (len(row_split[-1]) > y):
        return 'Not Okay'
    else:
        return 'Okay'


def dictionary_bifurcate(x):
    list_of_float_columns, list_of_varchar_columns = [], []
    for key, val in x.items():
        if type(x[key]) == tuple:
            list_of_float_columns.append([key] + [val])
        elif type(x[key]) == int:
            list_of_varchar_columns.append([key] + [val])

    return list_of_float_columns, list_of_varchar_columns


def driver():
    final_dict = eval(dict_columns_limit)
    list_of_float_columns, list_of_varchar_columns = dictionary_bifurcate(final_dict)
    for i in list_of_varchar_columns:
        print(i[0])
        store['result_' + i[0]] = store[i[0]].apply(lambda row: ddl_limit_varchar_handle(row, i[-1]))
        print(store[store['result_' + i[0]] == 'Not Okay'])
        print('******************************************************************************************')

    for i in list_of_float_columns:
        print(i[0])
        store['result_' + i[0]] = store[i[0]].apply(lambda row: ddl_limit_float_handle(row, i[-1][0], i[-1][-1]))
        print(store[store['result_' + i[0]] == 'Not Okay'])
        print('******************************************************************************************')

    print("\n\n", store.head())


if __name__ == '__main__':
    st = datetime.now()
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", help="Enter the csv file name")
    parser.add_argument("-dictionary", "-d", help="Enter the column names and limit")
    args = parser.parse_args()
    store = pl.read_csv(args.filename, encoding='utf8-lossy')
    dict_columns_limit = args.dictionary

    driver()
    et = datetime.now()
    print('Execution time: ', et - st)
