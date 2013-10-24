#控制流
#Python中有三种控制流语句——if, for和while
#if语句用来检验一个条件，若条件为真，运行if块，否则运行else块，但else块可选
#在Python中没有switch语句



#!/usr/bin/python
#Filename: if.py
number = 23;
guess = int(input('Enter an integer:'));

if guess == number:
    print("Congratulations, you guessed it.");#New block starts here
    print("But you do not win any prizes!");#New block ends here
elif guess < number:
    print("No, it is a little higher than that");#Another block
else:
    print("No, it is a little lower than that");

print("Done");
