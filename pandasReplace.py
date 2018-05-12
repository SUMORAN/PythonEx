# -*- coding:utf-8 -*-

import sys
from pandas import DataFrame
import pandas as pd

'''
dict_data_f1 = {}
dict_data_f2 = {}
dict_data_f3 = {}

with open("D:\\python\\datadl\\test1.txt", "r") as f1:
    for line in f1:
        for kv in [line.strip().split("\t")]:
            dict_data_f1.setdefault(kv[0],[]).append(kv[1])
print dict_data_f1

with open("D:\\python\\datadl\\test2.txt", "r") as f2:
    for line in f2:
        for kv2 in [line.strip().split("\t", 1)]:
            dict_data_f2.setdefault(kv2[0],[]).append(kv2[1])
print(dict_data_f2)

f1.close()
f2.close()
'''
#/home/zhangliang/GraduationPro/datadl/test1.txt
#d:\\python\\datadl\\
dict_data_f1 = pd.read_table("/home/zhangliang/GraduationPro/datadl/test/test.txt", sep='\t', names=["word", "type"])
dict_data_f2 = pd.read_table("/home/zhangliang/GraduationPro/datadl/test/testChar_1.txt", sep='\t', names=["word", "base","POStag", "chunktag", "NEtag"])
#print dict_data_f1
######dict_data_f1.to_csv("d:\\python\\datadl\\train\\train_new.csv",index=False)
#print("f2：\n",dict_data_f2)

dict_data_f2.drop_duplicates(subset="word", keep="first", inplace=True) #delete lines repeated
#print("f222：\n",dict_data_f2)
dict_data_f2.to_csv("/home/zhangliang/GraduationPro/datadl/dev/testfff2222.csv",index=False)

dict_data_f3 = pd.merge(dict_data_f1, dict_data_f2, how="left", on="word", sort=False)
#print dict_data_f3
dict_data_f3 = dict_data_f3[['word', 'base', 'POStag', 'chunktag', 'NEtag', 'type']]
#print dict_data_f3
#dict_data_f4 = dict_data_f3.loc[(dict_data_f3['POStag']=="")]
#print dict_data_f4
dict_data_f3.to_csv("/home/zhangliang/GraduationPro/datadl/test/test_out.csv",sep='\t', encoding="utf-8", index=False)
dict_data_f5 = dict_data_f3[['word', 'type']]
dict_data_f5.to_csv("/home/zhangliang/GraduationPro/datadl/test/test_new.csv",sep='\t', encoding="utf-8", index=False)

