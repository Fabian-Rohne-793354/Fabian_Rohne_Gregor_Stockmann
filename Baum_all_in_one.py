# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 13:41:15 2018

@author: Fabian Rohne
"""

from turtle import *
from random import *

def processString(n, oldString):
    newString = ""
    for ch in oldString:
        newString = newString + applyRules(n, ch)
        
    return newString 

def applyRules(n, ch):
    newString = ""
    if ch == "A":
        newString = '[-B-C][+B+C]'
        if n > 1:
            n = n - 1
            newString = processString(n, newString)
            newString = "A" + newString
        else: newString = "A" + newString
    elif ch == "B":
        x = random()
        print(x)
        if x < 0.25:
            newString = '[+B-B]'
        elif x < 0.5:
            newString = '[-B+B]'
        elif x < 0.7:
            newString = '[+B+C+C]'
        elif x < 0.9:
            newString = '[-B-C-C]'
        elif x < 1.0:
            newString = '[-C+C]'
        if n > 1: 
            n = n - 1
            newString = processString(n, newString)
            newString = "B" + newString
        else: newString = "B" + newString 
    elif ch == "C":
       x = random()
       print(x)
       if x < 0.25:
           newString = '[-C+C]'
       elif x < 0.5:
           newString = '[+C-C]'
       elif x < 0.7:
           newString = '[-C-D]'
       elif x < 0.9:
           newString = '[+C+D]'
       elif x < 0.95:
           newString = '[-C+E]'
       elif x < 1.0:
           newString = '[+C-E]'
       if n > 1: 
           n = n - 1
           newString = processString(n, newString)
           newString = "C" + newString
       else: newString = "C" + newString 
    else:
        newString = ch
    
    return newString

def Blatt():
    begin_fill()
    fillcolor('green')
    forward(5)
    left(45)
    forward(5)
    left(135)
    forward(5)
    left(45)
    forward(5)
    end_fill()
    
def Blüte():                #Blüte Code mit for-Schleife und n = n +1
    fillcolor('red')
    N = 5
    setheading(0)
    for n in range(N):
        begin_fill()
        forward(5)
        left(45)
        forward(5)
        left(135)
        forward(5)
        left(45)
        forward(5)
        right(191.2)
        n = n +1
        end_fill()
        


def drawLsystem(instructions, distance_1, distance_2, distance_3):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'A':
            forward(distance_1)
        elif cmd == 'B':
            forward(distance_2)
        elif cmd == 'C':
            forward(distance_3)
        elif cmd == 'D':
            Blatt()
        elif cmd == 'E':
            Blüte()
        elif cmd == '+':
            right(gauss(25,5))
        elif cmd == '-':
            left(gauss(25,5))
        elif cmd == '[':
            savedInfoList.append([heading(), xcor(), ycor()])
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            setheading(newInfo[0])
            up()
            setposition(newInfo[1], newInfo[2])
            down()

def main():
    inst = processString(8, "A")   # create the string
    print(inst)

    penup()
    goto(0,-250)
    pendown()
    left(90)
    speed(0)
    drawLsystem(inst, 30, 20, 10)   # draw the picture
    done()
    # angle 60, segment length 5
    exitonclick()

main()