#!/usr/bin/python
#掷骰子游戏
#游戏规则：玩家投掷两个骰子，每个骰子6个面，1-6，掷完骰子后，计算两个骰子的和。
#如果首次的和是7或者11，那儿玩家赢；
#如果首次的和是2,3或者12，那么玩家输，庄家赢；
#如果首次投掷的和是4,5,6,8,9,10,那么这个和就成为玩家的“点数”，
#想要赢的话，玩家必须连续的投掷骰子，直到投掷的和等于“点数”为止；
#但是如果中途投掷的和是7，那么玩家输！

#Filename: guess.py
#-*-encoding:utf-8-*-
import random
import time

def gennum():
    random.seed(time.time())
    dice={}
    dice['1']=random.randrange(6)+1
    dice['2']=random.randrange(6)+1
    return sum(dice.values())

numsum=gennum()

if numsum in [7,11]:
    print("恭喜！你赢啦，点数是 %d，看来你今天运气不错，去买张彩票试试吧！" % numsum)
elif numsum in [2,3,12]: #craps
    print("抱歉，你输了，点数是 %d，没关系，第一次嘛" % numsum)
else:
    print("现在进入循环投掷阶段，你需要掷出%d才能赢" % numsum)
    counter=0
    while True:
        num=gennum()
        if num == 7:
            print("抱歉!你输了，点数是 %d" % num)
            break
        elif num == numsum:
            print("恭喜!你赢啦，点数是 %d" % num)
            break
        else:
            print("抱歉，点数是 %d,请再试一次吧" % num)
            time.sleep(3)
            counter+=1
            if counter > 5:
                print("今天运气不好，选个黄道吉日再来吧！")
                break
            elif counter == 3:
                print("看来你今天运气不太好啊！")
            continue
