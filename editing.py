"""
This script binarizes the data in a csv.

"""
# coding: utf-8
import pandas as pd
import numpy as  np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import csv
import sys
import argparse

print('         .       ')
print('         .       ')
print(' Loading the csv ')
print('         .       ')
print('         .       ')

#Reading a csv file
parser = argparse.ArgumentParser('Files')
parser.add_argument('-i','--file')
parser.add_argument('-o','--output')
f_args = parser.parse_args()
input_csv = f_args.file
output_csv = f_args.output
print('in:',input_csv)
print('out:',output_csv)
def Binarization(input_csv, output_csv):
    data = pd.read_csv(input_csv, encoding='Shift-JIS').values.tolist()
    print('==========================')

    print('#Loaded data from the csv#')
    print('--------------------------')

    print(data)
    print('==========================')
    ingre_sep=[]

    for i in range(len(data)):
        ingre_sep.append(data[i][1].split('、'))

    ingre_sep_f=list(itertools.chain.from_iterable(ingre_sep))
    ingre_unique_list=(np.unique(ingre_sep_f)).tolist()

    print('         .       ')
    print('         .       ')
    print('Modifying the data')
    print('         .       ')
    print('         .       ')

    modified_data=[]
    #Giving the variables to modified_data which is to be converted in a csv file
    variables = ['name']+ingre_unique_list
    modified_data.append(variables)
    #Setting values for each column, 'j'th one.
    for j in range(len(data)):
        renewed_data=[]
        renewed_data.append(data[j][0])
        for i in range(len(ingre_unique_list)):
            #converting imformation whether each ingredient is included in the product or not, 0 or 1, so called binarization.

            if ingre_unique_list[i] in ingre_sep[j]:
                renewed_data.append(1)
            else:
                renewed_data.append(0)
        modified_data.append(renewed_data)

    print('==========================')

    print('#Data-modifying completed#')
    print('--------------------------')

    print(modified_data)
    print('==========================')
    input_csv
    with open(output_csv, 'w', encoding='Shift-JIS') as f:
        for i in range(len(modified_data)):
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(modified_data[i])
    print('         .       ')
    print('         .       ')
    print('--------------------------')
    print('#You have obtained ['+ output_csv +'] in the current directory')
    print('--------------------------')

    return pd.read_csv(output_csv, encoding='Shift-JIS').values.tolist()


if (not input_csv) or (not output_csv):
    print('========================================================================================================')
    print('==========================================-------NOTICE-------==========================================')
    print('')
    print(' Usage example for this script : python editing_csv.py -i (input csv file name) -o (output csv file name)')
    print('')
    print('========================================================================================================')

else:
    print('=========================')
    print('~Do you want to select files?~')
    print('=========================')

    print('a: Yes')
    print('b: No, files are already choosen')
    mode = input("a or b:")
    if mode == 'a':
        input_f = input("Choose the file to convert:")
        output_f = input("Name the file to export:")
    elif mode == 'b':
        pass
    else:
        print('invalid answer')
        exit(0)
Bidernization(input_csv, output_csv)