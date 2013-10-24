#!/usr/bin/python
#使用模块在其他程序中重用很多函数，模块是一个包含所有定义的函数和变量的文件。
#为了在其他程序中重用模块，模块的文件名必须以.py为扩展名。
#sys.argv包含了命令行参数的列表，即使用命令行传递给程序的参数，脚本的名称总是sys.argv列表的第一个参数。
#sys.path包含输入模块的目录名列表。



#Filename: using_sys.py
import sys;

print("The command and line arguments are: ");
for i in sys.argv:
    print(i);

print("\n\nThe Python Path is", sys.path, "\n");
