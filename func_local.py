#!/usr/bin/python
#变量的作用域
#使用局部变量



#Filename: func_local.py
def func(x):
    print("x is ", x);
    x = 2;
    print("Changed local x to ", x);

x = 50;
func(x);

print('x is still ', x);
