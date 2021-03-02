"""
This script is for creating a csv file and collecting data.

"""

# coding: utf-8

#文字コードの指定
import csv
csv_filename='new2.csv'
file = open(csv_filename, 'w', encoding='UTF-8')    #Create a non-existing file name.
w = csv.writer(file, lineterminator='\n')
#特徴項目のリスト　何を特徴数として記録するかEXCEL手作業？になりそう
w.writerows([['Goods name','character１','character2']])

goods_list = [[1,2,3],[2,5,6],[5,7,2]]
"""
ここでスクレイピング取得情報をリストappend
"""
#cvsにデータ追加

file.close()

for i in range(len(goods_list)):
    with open(csv_filename, 'a', encoding='UTF-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        print(i)
        print(goods_list[i])
        writer.writerow(goods_list[i])

