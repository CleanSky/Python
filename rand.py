#!/usr/bin/python
#随机生成整数

#Filename: rand.py
import random

def getResultStr(totalCount, resultCount):
	elements = [x + 1 for x in range(totalCount)]
	retStr = ''
	for i in range(resultCount):
		res = elements[random.randint(0, len(elements)-1)]
		elements.remove(res)
		retStr += ' ' + str(res)

	return retStr

#双色球
print(getResultStr(33, 6));
print(getResultStr(16, 1));
#大乐透
print(getResultStr(35, 5));
print(getResultStr(12, 2));
