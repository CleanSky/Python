#!/usr/bin/python
#字符串去重复值

#Filename: filter_same.py
a='32546743624577996'
b=set(a)
print(b.__len__()) #得到字串不同值的个数
print(''.join(b)) #得到去重复后不同值的组合字串
