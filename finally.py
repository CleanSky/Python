#!/usr/bin/python
#在读一个文件时，若希望在无论异常发生与否的情况下都关闭文件，可以用finally块来完成。
#在一个try块下，可以同时使用except从句和finally块，若要同时使用它们，需要把一个嵌入另外一个。



#Filename: finally.py
import time;

try:
    f = open('poem.txt');
    while True:#our usual file-reading idiom
        line = f.readline();
        if len(line) == 0:
            break;
        time.sleep(2);
        print(line, end="");
finally:
    f.close();
    print("Cleaning up...closed the file");
