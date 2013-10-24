#!/usr/bin/python
#每个模块都有一个名称，在模块中可以通过语句找出模块的名称。
#使用模块的__name__属性可以实现在程序被使用时运行主块，而在它被别的模块输入时不运行主块。



#Filename: using_name.py
if __name__ == "__main__":
    print("This program is being run by itself");
else:
    print("I am being imported from another module");
