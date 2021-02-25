"""
This script is for creating a csv file and collecting data.

"""
import csv
csv_filename='new.csv'
file = open(csv_filename, 'w')    #Create a non-existing file name.
w = csv.writer(file)
#特徴項目のリスト　何を特徴数として記録するかEXCEL手作業？になりそう
w.writerows(['商品名','参照項目１','参照項目１'])

goods_list = []
"""
ここでスクレイピング取得情報をリストappend
"""
#cvsにデータ追加
with open(csv_filename, 'a') as f:
    for i in ranege(len('goods_list')):
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(goods_list[i])

file.close()