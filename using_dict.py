#!/usr/bin/python
#字典类似于通过联系人名字查找地址和联系人详细情况的地址簿，即把键（名字）和值（详细情况）联系在一起。
#键必须唯一，只能使用不可变的对象（如字符串）作为字典的键。
#键值对在字典中以这样的方式标记：d = {key1:value1, key2:value2}
#键值对用冒号分割，而各个对用逗号分割，所有这些包括在花括号中。
#字典中的键值对是没有顺序的。
#字典是dict类的实例/对象。



#Filename: using_dict.py
#'ab' is short for 'a'ddress'b'ook

ab = {'Swaroop':'swaroopch@byteofpython.info',
      'Larry':'larry@wall.org', 
      'Matsumoto':'matz@ruby-lang.org',
      'Spammer':'spammer@hotmail.com'};
print("Swaroop's address is %s"% ab['Swaroop']);

#Adding a key/value pair
ab['Guido'] = 'guido@python.org';

#Deleting a key/value pair
del ab['Spammer'];

print('\nThere are %d contacts in the address-book\n' %len(ab));
for name, address in ab.items():
    print("Contact %s at %s" %(name, address));

if 'Guido' in ab:#OR ab.has_key('Guido')
    print("\nGuido's address is %s" %ab['Guido']);
