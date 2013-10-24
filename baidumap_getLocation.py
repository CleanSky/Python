#!/usr/bin/python

#Filename: baidumap_getLocation.py
import baidumap

bm=xBaiduMap()
print(bm.getLocation("红旗大街淮河路",'哈尔滨'))
print(bm.getLocation("人民路沙浦路"))
print(bm.getLocation("人民路沙浦路",'广州'))
print(bm.getAddress(30.690714,104.079473))       
