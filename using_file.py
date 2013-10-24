#!/usr/bin/python
#使用文件
#创建一个file类的对象来打开一个文件，分别使用file类的read、readline或write方法来恰当地读写文件，对文件的读写能力依赖于打开文件时指定的模式。最后使用close方法关闭文件。



#Filename: using_file.py
poem = '''\
Programming is fun.
When the work is done,
if you wanna make your work also fun:
    use Python!
''';

f = open('poem.txt', 'w');#open for 'w'riting
f.write(poem);#write text to file
f.close();#close the file

f = open('poem.txt');#if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline();
    if len(line) == 0:#Zero length indicates EOF
        break;
    print(line, end="");
f.close();#close the file
