#!/usr/bin/python
#数：在Python中有4种类型的数——整数、长整数、浮点数和复数，如2,123456,3.23E-4,(-5+4j)
#字符串：字符的序列，每个Python程序中都要用到字符串
#单引号(')，双引号(")
#三引号('''or""")：可以指示一个多行的字符串，可以在三引号中自由使用单引号和双引号
#转义符：反斜杠\，\\表示反斜杠本身
#在一个字符串中，行末的单独一个反斜杠表示字符串在下一行继续，而不是开始一个新的行。
#自然字符串：通过给字符串加上前缀r或R来指定，如r"New lines are indicated by\n"
#Unicode字符串：通过给字符串加上前缀u或U来指定，如u"This is a Unicode string.ChainMap当处理文本文件时使用Unicode字符串，尤其是当文件含有非英语语言时。
#字符串是不可变的
#按字面意义级联字符串：如果把两个字符串按字面意义相邻存放，则python会自动级联
#Python中没有专门的char数据类型
#变量是标识符的例子，标识符是用来标识某样东西的名字。字母、下划线、数字，大小写敏感。
#变量可以处理不同类型的值，称为数据类型，基本数据类型有数和字符串。可以用类来创造自己的类型。
#Python把程序中用到的任何东西都称为对象，一般说“某个对象”
#使用变量时只需要给他们赋值，不需要声明或定义数据类型
#逻辑行：Python看见的单个语句；物理行：编写程序时所看见的语句；Python假定每个物理行对应一个逻辑行。
#缩进：Python中的行首空白是重要的，同一层次的语句必须有相同的缩进，每一组这样的语句称为一个块。错误的缩进会引发错误。



#Filename: var.py
i=5
print(i)
i=i+1
print(i)

s='''This is a multi-line string.
This is the second line.'''
print(s)