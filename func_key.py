#!/usr/bin/python
#若函数有多个参数，而只想指定其中的一部分，则可以通过命名来为这些参数赋值（关键参数），即使用名字（关键字）而非位置来给参数指定实参。
#优点：不必担心参数的顺序；假设其他参数都有默认值，可以只给想要的那些参数赋值。



#Filename: func_key.py
def func(a, b = 5, c = 10):
    print("a is ", a, " and b is ", b, " and c is ", c);

func(3, 7);
func(25, c = 24);
func(c = 50, a = 100);
