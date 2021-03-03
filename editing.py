"""
This script is for converting csv and modifying data to quantify features and to interpolate missing values.

"""
# coding: utf-8
import pandas as pd
import numpy as  np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
print('         .       ')
print('         .       ')
print(' Loading the csv ')
print('         .       ')
print('         .       ')

#Reading a csv file

data = pd.read_csv('ingredient.csv', encoding='Shift-JIS').values.tolist()
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
        #converting imformation whether each ingredient is included in the product or not, 0 or 1, so called bidernization.

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
