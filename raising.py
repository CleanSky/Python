#!/usr/bin/python
#可以使用raise语句引发异常，需要指明错误/异常的名称和伴随异常触发的异常对象。
#引发的错误或异常应该分别是一个Error或Exception类的直接或间接导出类。



#Filename: raising.py
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self);
        self.length = length;
        self.atleast = atleast;

try:
    s = input("Enter something:");
    if len(s) < 3:
        raise ShortInputException(len(s), 3);
    #Other work can also continue as usual here.
except EOFError:
    print("\nWhy did you do an EOF on me?");
except ShortInputException:
    print("ShortInputException: The input was of length %d, was expecting at least 3." %len(s));
else:
    print("No exception was raised.");
