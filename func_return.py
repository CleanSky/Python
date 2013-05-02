#!/usr/bin/python
#return语句用来从一个函数返回，即跳出函数，从函数返回一个值。
#pass语句表示一个空的语句块



#Filename: func_return.py
def maximum(x, y):
    if x > y:
        return x;
    else:
        return y;
    pass

print(maximum(2, 3));
