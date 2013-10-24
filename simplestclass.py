#!/usr/bin/python
#面向对象的编程，面向过程的编程
#类创建一个新类型，对象是类的实例。
#属于一个对象或类的变量被称为域，域和方法合称为类的属性。
#域有两种类型——属于每个实例/类的对象或属于类本身，分别被称为实例变量和类变量。
#类使用class关键字创建，类的域和方法被列在一个缩进块中。
#类的方法和普通函数有一个区别：必须有一个额外的第一个参数名称，但调用该方法时不必为该参数赋值，Python会提供这个值。




#Filename: simplestclass.py
class Person:
    pass;#An empty block

p = Person();
print(p);