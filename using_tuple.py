#!/usr/bin/python
#元组和列表十分类似，但是元组和字符串一样是不可变的，即不能修改元组。
#元组同U哦圆括号中庸逗号分割的项目定义。
#元组通常用在使语句或用户定义的函数能够安全地采用一组值的时候，即被使用的元组的值不会改变。



#Filename: using_tuple.py
zoo = ("wolf", "elephant", "penguin");
print("Number of animals in the zoo is", len(zoo));

new_zoo = ("monkey", "dolphin", zoo);
print("Number of animals in the new zoo is", len(new_zoo));
print("All animals in new zoo are", new_zoo);
print("Animals brought from old zoo are", new_zoo[2]);
print("Last animal brought from old zoo is", new_zoo[2][2]);
