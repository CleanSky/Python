# -*- coding: cp936 -*-
import os    # 引入os模块

# 跨平台的行结束符，由于接下来在循环中经常使用，故用一个本地变量来替换模块变量以提高效率
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
