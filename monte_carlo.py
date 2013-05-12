#!/usr/bin/python
#蒙特卡罗法又称随机抽样技巧法或统计试验法，，其基本原理如下：
#由概率定义知，某事件的概率可以用大量试验中该事件发生的频率来估算，
#当样本容量足够大时，可以认为该事件的发生频率即为其概率。
#
#考虑平面上的一个边长为r的正方形及其内切圆，如何求出这个“图形”的面积呢？
#Monte Carlo方法是这样一种“随机化”的方法：
#向该正方形“随机地”投掷N个点，而落于圆内的点数为M，
#则下列等式约成立：PI*(r/2)*(r/2)/r*r=M/N 故PI=4*M/N。

#Filename: monte_carlo.py
from random import random

n=10**6
print(sum(1 if random()**2 + random()**2 < 1 else 0 for i in range(n))*4.0/n)
