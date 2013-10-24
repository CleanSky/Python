#!/usr/bin/python
#continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环



#Filename: continue.py
while True:
    s = input("Enter something:");
    if "quit" == s:
        break;
    if len(s) < 3:
        continue;
    print("Input is of sufficient length");

print("Done");
