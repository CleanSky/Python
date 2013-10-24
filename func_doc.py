#!/usr/bin/python
#DocStrings是一个重要的工具，他帮助程序文档更加简单易懂，可以在程序运行的时候，从函数恢复文档字符串。



#Filename: func_doc.py
def printMax(x, y):
    '''Print the maximum of two numbers.
    The two values must be integers.'''
    x = int(x)#convert to integers, if possible
    y = int(y)

    if x > y:
        print(x, " is the maximum");
    else:
        print(y, " is the maximum");


printMax(3, 5);
print(printMax.__doc__);
