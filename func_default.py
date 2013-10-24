#!/usr/bin/python
#对于一些函数，可能希望它的一些参数是可选的，若用户不想为这些参数提供值，这些参数就使用默认值。
#可以在函数定义的形参名后加上赋值运算符和默认值，从而给形参指定默认参数值。
#默认参数值应该是一个参数，是不可变的。
#只有在形参表末尾的那些参数可以有默认参数值，即声明函数形参时，不能先声明有默认值的形参后声明无默认值的形参。



#Filename: func_default.py
def say(message, times = 1):
    print(message * times);

say("Hello");
say("World", 5);
