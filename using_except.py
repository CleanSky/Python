#!/usr/bin/python
#异常信息：异常类型+异常地点
#当异常产生时，如果有代码来处理它，Python对其进行缺省处理，输出一些异常信息并终止程序。
#程序在执行的过程中产生异常，但不希望程序终止执行，这时可以用try和except语句对异常进行处理。



#Filename: using_except.py
filename = '';

while 1:
    filename = input("Input a file name: ");
    if filename == 'q':
        break;
    try:
        f = open(file, "r");
        print("Opened a file.");
    except:
        print("There is no file named", filename);

def inputAge():
    age = int(input("Input your age: "));
    if (age > 100 or age < 18):
        raise;
    return age;

inputAge();
