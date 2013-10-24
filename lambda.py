#!/usr/bin/python
#Python允许定义一种单行的小函数，叫lambda函数。
#定义lambda函数的形式：lambda 参数: 表达式
#lambda函数可以接受任意个参数，包括可选参数，但表达式只有一个。
#如果函数非常简单，只有一个表达式，不包括命令，可以考虑用lambda函数。

#Filename: lambda.py
g = lambda x, y: x * y;
print(g(3, 4));

g = lambda x, y = 0, z = 0: x + y + z;
print(g(1));
print(g(3, 4, 7));
