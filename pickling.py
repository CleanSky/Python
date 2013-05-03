#!/usr/bin/python
#Python提供一个标准的模块，成为pickle。使用它，可以在一个文件中存储任何Python对象，之后可以把它完整无缺地取出来，这被称为持久地存储对象。
#另一个模块成为cPickle，功能和pickle模块完全相同，只不过它是用C语言编写的，比pickle块1000倍。



#Filename: pickling.py
#import cPickle as p;#Python3.x中移除了cPickle模块，可以使用pickle模块代替
import pickle as p

shoplistfile = "shoplist.data";
#the name of the file whre we will store the object

shoplist = ['apple', 'mango', 'carrot'];

#Write to the file
f = open(shoplistfile, 'wb');#二进制打开
p.dump(shoplist, f);#dump the object to a file
f.close();

del shoplist;#remove the shoplist

#Read back from the storage
f = open(shoplistfile, 'rb');#二进制打开
storedlist = p.load(f);
print(storedlist);
