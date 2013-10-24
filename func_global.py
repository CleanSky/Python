#!/usr/bin/python
#使用global语句可以清楚地表明变量是在外面的块定义的



#Filename: func_global.py
def func():
    global x;

    print("x is ", x);
    x = 2;
    print("Changed local x to ", x);

x = 50;
func();
print("Value of x is ", x);
