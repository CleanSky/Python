# -*- coding: cp936 -*-
import os    # ����osģ��

# ��ƽ̨���н����������ڽ�������ѭ���о���ʹ�ã�����һ�����ر������滻ģ����������Ч��
ls = os.linesep

# get filename
fname = raw_input("Enter the filename: ")

# judge whether the file exists or not
while True:
    if os.path.exists(fname):
        print "Error: '%s' already exists" % fname
    else:
        break

# get file content lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()

print 'DONE'
