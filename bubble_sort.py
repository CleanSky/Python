#!/usr/bin/python
#冒泡排序

#Filename: bubble_sort.py
def bubble(list):
    flag=1
    tail=len(list)-1
    while(flag):
        flag=0
        for i in range(tail):
            if list[i]>list[i+1]:
                t=list[i]
                list[i]=list[i+1]
                list[i+1]=t
                flag=1
                pass
            pass
        tail-=1
        pass
    return list
list=[1,3,4,19,7,234,19.22,223344,0x2333]
if __name__=="__main__":
    print(bubble(list))
