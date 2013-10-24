#!/usr/bin/python
#当创建一个对象并给它赋一个变量时，这个变量仅仅引用那个对象，而不是表示对象本身。
#变量名指向计算机中存储那个对象的内存，这被称作名称到对象的绑定。



#Filename: reference.py
print("Simple Assignment");
shoplist = ['apple', 'mango', 'carrot', 'banana'];
mylist = shoplist;#mylist is just another name pointing to the same object

del shoplist[0];

print("shoplist is", shoplist);
print("mylist is", mylist);
#notice that both shoplist and mylist print the same list without the 'apple'

print("Copy by making a full slice");
mylist = shoplist[:];#make a copy by doing a full slice
del mylist[0];#remove the first item

print("shoplist is", shoplist);
print("mylist is", mylist);
#notice that now the two lists are different
