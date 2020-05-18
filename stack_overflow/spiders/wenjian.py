import numpy as np
import pandas as pd
import csv

filepath = "file:///C:/spider/export.csv"
#y = int(k1.get())
#z = k2.get()
# 打开文件
# df = pd.read_csv(filepath, header=0, skip_blank_lines=True, encoding="utf-8")
df = pd.read_csv(filepath, header=0, sep=',', skip_blank_lines=True)
# gender = df.groupby('_qv_vote')
gender = df.sort_values(by='_qv_vote', ascending=False)
type(gender)
gender.count()
print(gender)
gender2 = gender[gender['_qv_content'].str.contains('at')]
print(gender2)
wj = gender2.head(5)
print(wj)

# 对问题vote数列降序排列
# df.sort_values(by='_qv_vote', axis=0, ascending=False, inplace=True, na_position='last')
# 存储还需要修改
# wj.to_csv(filepath, index=False, header=False)
print('Hello World!')