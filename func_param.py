#!/usr/bin/python
#使用函数形参



#Filename: func_param.py
def printMax(a, b):
    if a > b:
        print(a, " is the maximum.");
    else:
        print(b, " is the maximum.");

printMax(3, 4);#directly give literal values

x = 7;
y = 5;
printMax(x, y);#give variables arguments
