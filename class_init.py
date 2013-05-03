#!/usr/bin/python
#Python类中有很多方法的名字有特殊的重要意义。
#__init__方法在类的一个对象被建立时，马上运行，该方法可以用来对你的对象做一些希望的初始化。



#Filename: class_init.py
class Person:
    def __init__(self, name):
        self.name = name;
    def sayHi(self):
        print("Hello, my name is", self.name);

p = Person('Swaroop');
p.sayHi();#Or Person('Swaroop').sayHi();
