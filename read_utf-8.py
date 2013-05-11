#!/usr/bin/python
#Python 读写unicode文件

#Filename: read_utf-8.py
#coding=utf-8 

import os 
import codecs 

#以utf-8编码打开并写文件
def writefile(fn, v_ls): 
    f = codecs.open(fn, 'wb', 'utf-8') #以utf-8编码的二进制写文件方式打开文件
    for i in v_ls: #写入文件
        f.write(i + os.linesep) 
    f.close() #关闭文件

#以utf-8编码打开并读文件
def readfile(fn): 
    f = codecs.open(fn, 'r','utf-8') 
    ls = [ line.strip() for line in f] #读文件
    f.close() 
    for i in ls: #输出
        print(i) 

if __name__ == '__main__': 
    fn = u'11.txt' #unicode编码
    ls = [u'1.python', u'2.how to pythonic', u'3.python cook', u'python编程'] 
    writefile(fn, ls) 
    readfile(fn)
