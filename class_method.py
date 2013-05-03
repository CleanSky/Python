#!/usr/bin/python
#类/对象可以拥有函数一样的方法，只不过需要有一个额外的self变量。



#Filename: method.py
class Person:
    def sayHi(self):
        print("Hello, how are you?");

p = Person();
p.sayHi();#It can also be written as Person().sayHi();
