"""
This script is for converting csv and modifying data to quantify features and to interpolate missing values.

"""
# coding: utf-8
import pandas as pd
import numpy as  np
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
print('         .       ')
print('         .       ')
print('         .       ')
print('         .       ')
print('         .       ')
print('         .       ')

# データをpd.DataFrame形式で読み込む
parser = argparse.ArgumentParser('Example program')
parser.add_argument('-f','--file')
f_args = parser.parse_args()
file_to_open = f_args.file
print(file_to_open)
if not file_to_open:
    df = pd.read_csv("new2.csv", encoding='UTF-8')#header=None, ヘッダの使用可否
else:
    df = pd.read_csv(file_to_open, encoding='UTF-8')
print(df['Sex'])
#df.iloc[0].to_list() 行をリストとして抽出
#df['特徴数'].to_list()　列をリストとして抽出


#df = org_file(columns=columns_name)
print('=============================================================')
print('dataframe loaded')
print('=============================================================')
#org_file.columns=org_file.index[0]
#print(org_file.columns)
#org_file.drop(index=0))

#showing the contents of dataframe
contents_d=df.head(8)
print('contents of dataframe')
print('-------------------------------------------------------------')
print(contents_d)
print('=============================================================')
# 各特徴量の欠損値をカウント
sum_d=df.isnull().sum()
print('=============================================================')
print('The number of the missing values')
print('-------------------------------------------------------------')
print(sum_d)
print('=============================================================')
#欠損値に対する処理
"""
# 欠損値を含む行を削除
df.dropna()

# 特徴項目Xに欠損があるサンプルのみ削除する
df.dropna(subset=['特徴項目X'])

# 欠損していない値がn個以上あるサンプルのみを残して削除
df.dropna(thresh=n)

# 補完
df.fillna(P)
====Pに入るオプション====
df.mean()：その特徴数の平均値
実数：任意

# 線形補完
ip = df.interpolate(method='linear')
ip　　たぶん使うことない

df = pd.concat([df_data, df_target], axis=1)      項目の追加
=======================
"""


#数値でない特徴量の定量化
"""
#物理的、または、性質的に順序を持つ特徴量（例：服のサイズ、暦の名前）
# マッピングの実行
#辞書の生成例
size_mapping = {'A':1, 'B':2, 'C':3, 'D':4}
df['特徴項目'] = df['特徴項目'].map(size_mapping)
df

#物理的、または、性質的に順序を持たない特徴量（例：服のサイズ、暦の名前）
# pandasでone-hotエンコーディング。ダミー変数を作成
pd.get_dummies(df['特徴項目'])
"""
#dataframeの保存
#df.to_csv("任意.csv")