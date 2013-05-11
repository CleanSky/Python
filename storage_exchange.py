#!/usr/bin/python
#存储空间单位转换

#Filename: storage_exchange.py
diskunit=['Byte','KB','MB','GB','TB','PB','EB']

def byteformat(size,unit='Byte'):
    """將文件大小轉換為合適的單位表示."""
    if size<1024: return '%.2f %s' % (size,unit)
    
    return byteformat(size/1024.0,diskunit[diskunit.index(unit)+1])

print(byteformat(10243424325))
