#!/usr/bin/python
#list是处理一组有序项目的数据结构，即可以在一个列表中存储一个序列的项目。
#列表中的项目应该包括在方括号中，可以添加、删除、搜索列表中的项目，列表是可变的数据类型。
#Python为list类提供了append方法。
#类也有域，它是仅仅为类而定义的变量，仅仅在有一个该类的对象时，才可以使用这些变量/名称，类也通过点号使用。



#Filename: using_list.py
#This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana'];

print("I have", len(shoplist), 'items to purchase.');

print("These items are:", end="");#end=""取消自动换行打印功能
for item in shoplist:
    print(item, end=" "),
print("\nI also have to buy rice.");
shoplist.append("rice");#将rice附加到购物列表中
print("My shopping list now is", shoplist);

print("I will sort my list now");
shoplist.sort();#对列表中的元素按字典排序
print("Sorted shopping list is", shoplist);

print("The first item I will buy is", shoplist[0]);
olditem = shoplist[0];
del shoplist[0];#删除列表中的某个元素
print("I bought the", olditem);
print("My shopping list now is", shoplist);
