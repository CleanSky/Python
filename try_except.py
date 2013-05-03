#!/usr/bin/python
#可以使用try...except语句处理异常，把通常的语句放在try-块中，而把错误处理语句放在except-块中。



#Filename: try_except.py
import sys

try:
    s = input("Enter something:");
except EOFError:
    print("\nWhy did you do an EOF on me?");
    sys.exit();#exit the program
except:
    print("\nSome Error/exception occurred.");
    #here, we are not exiting the program.

print("Done");
