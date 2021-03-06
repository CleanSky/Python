#!/usr/bin/python
#大致是这样的：1000瓶无色无味的液体，其中一瓶为毒药，其它皆为清水，毒药只取一滴与清水混合为一瓶也可以毒死兔子。现在有10只兔子，当兔子喝下毒药两个小时后死去，请设计一种方案，能够在24小时内找到这瓶毒药。
#    ................2分钟后
#    前面的问题你一定想清楚了，那么略改动一下：1000瓶无色无味的液体，其中一瓶为毒药，其它皆为清水，毒药只取一滴与清水混合为一瓶也可以毒死兔子。现在有10只兔子，当兔子喝下毒药20个小时后死去，请设计一种方案，能够在24小时内找到这瓶毒药。
#     ................2分钟后
#    有多种方法，比如我每隔5分钟给兔子喝一次100瓶液体混合在一起的东西，根据兔子死去的先后顺序，就可以判断是那一瓶了。
#
#    有没有更好的办法呢，我这里仅仅提供一种时间最优的方法，也就是在20个小时找到这瓶毒药。当然也可以有死的兔子最少，在死去兔子和时间找到一个最佳折中点的优化问题。
#    方法如下：
#    给10只兔子编号1－10，每只兔子代表一个数，列表如下： 
#    编号    1    2    3    4    5    ...    10
#    数字    1    2    4    8    16    ...    512
#    
#    瓶子也有编号，依次为1－1000。    呵呵，聪明的你应该知道我要怎么做了吧，不过我还是要说下去，并写python代码来实现。
#    我希望是当编号为Y1,Y2,Y3...的兔子死去时，可以推导出编号为X瓶子为毒药。比如编号为1,2,4的兔子死去，那就得知 兔子对应的数字 为1＋2＋8＝11，就是编号为11的瓶子是毒药。比如编号为1,4，10的兔子死去，那就得知 兔子对应的数字 为1＋8＋512＝521，就是编号为521的瓶子是毒药。
#    现在的问题就是要知道编号不同的每只兔子要喝哪几瓶液体。

#Filename: rabbit_poision.py
def main():
    """
    baselist是兔子编号从1－10对应的数字，result是最终每只兔子要喝的液体
    """
    baselist=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512];
    result=[[], [], [], [], [], [], [], [], [], []];
    for water in range(1, 1001):
        watertmp=water;
        for i in range(9, -1, -1):
            if (watertmp-baselist[i])>=0:
                watertmp -= baselist[i];
                result[i].append(water);
    for i in range(1, 11):
        print("The Num %d rabit need drink the next liquid " %(i+1));
    pass;

if __name__=="__main__":
    main();
