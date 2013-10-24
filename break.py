#!/usr/bin/python
#break语句是用来终止循环语句的，如果从for或while循环中终止，任何对应的循环else块将不执行。



#Filename: break.py
while True:
    s = input("Enter something:");

    if "quit" == s:
        break;
    print("Length of the string is ", len(s));

print("Done");
