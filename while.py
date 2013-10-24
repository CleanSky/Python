#!/usr/bin/python
#只要在一个条件为真的情况下，while语句允许你重复执行一块语句。while语句有一个可选的else从句。



#Filename: while.py
number = 23;
running = True;

while running:
    guess = int(input("Enter an integer:"));

    if guess == number:
        print("Congratulations, you guessed it.");
        running = False;#This causes the while loop to stop
    elif guess < number:
        print("No, it is a bit higher than that.");
    else:
        print("No, it is a bit lower than that.");
else:
    print("There is an 'else' cause in the while loop");

print("Done");
