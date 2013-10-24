#!/usr/bin/python
#序列的两个主要特点是索引操作符合切片操作符。
#索引操作符让我们可以从序列中抓取一个特定项目。
#切片操作符让我们能够获取序列的一个切片，即一部分序列。
#下标操作：使用索引来取得序列中的单个项目。
#索引可以是负数，只不过位置是从序列尾开始计算的，-1表示倒数第一个元素。
#切片操作符是序列号后跟一个方括号，方括号中有一对可选的数字，并用冒号分割。
#如果想复制一个列表或类似的序列或其他复杂的对象（不是整数那样的简单对象），那么必须使用切片操作符来取得拷贝。



#Filename: seq.py
shoplist = ['apple', 'mango', 'carrot', 'banana'];

#Indexing or Subscription operation
print("Item 0 is", shoplist[0]);
print("Item 1 is", shoplist[1]);
print("Item 2 is", shoplist[2]);
print("Item 3 is", shoplist[3]);
print("Item -1 is", shoplist[-1]);
print("Item -2 is", shoplist[-2]);

#Slicing on a list
print("Item 1 to 3 is", shoplist[1:3]);
print("Item 2 to end is", shoplist[2:]);
print("Item 1 to -1 is", shoplist[1:-1]);
print("Item start to end is", shoplist[:]);

#Slicing on a string
name = "swaroop";
print("characters 1 to 3 is", name[1:3]);
print("characters 2 to end is", name[2:]);
print("characters 1 to -1 is", name[1:-1]);
print("characters start to end is", name[:]);
