#!/usr/bin/python
#一句话打印舅舅乘法表

#Filename: double_nine_table.py
print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]));
