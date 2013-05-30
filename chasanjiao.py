#!/usr/bin/python

#Filename: chasanjiao.py
from time import time
import itertools

t1=time()

n=5
k=n*(n+1)/2

def fun(a):
    t=a
    for i in range(n):
        yield t
        t=[abs(t[i]-t[i-1]) for i in range(1,len(t))]

def main():
    for i in itertools.permutations(range(1, k+1), n):
        t=list(fun(i))
        if len(set( [j for i in t for j in i] ))==k:
            print(t)
main()

print(time()-t1)
