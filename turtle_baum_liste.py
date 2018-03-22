# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:14:11 2018

@author: xReinheitsgebotx
"""

from turtle import *                                                      # importiert alles aus dem Modul turtle
from random import *                                                      # importiert alles aus dem Modul random
 
def Blatt():                                                              # definiert die Funktion 'Blatt'
    begin_fill()                                                          # beginnt das Füllen 
    fillcolor('green')                                                    # setzt die Füllfarbe auf grün
    forward(5)                                                            # zeichnet eine Raute   
    left(45)                                                              
    forward(5)                                                            
    left(135)                                                             
    forward(5)                                                            
    left(45)                                                              
    forward(5)                                                            
    end_fill()                                                            # beendet das füllen 
     
def Blüte():                                                              # definiert die Funktion 'Blüte' 
    fillcolor('red')                                                      # setzt die Füllfarbe auf rot
    N = 5                                                                 # weist 'N' 5 zu 
    setheading(0)                                                         # setzt Blickrichtung der Turtle nach oben 
    for n in range(N):                                                    # die folgende Anweisung word 5-mal hinter einander aus geführt
        begin_fill()                                                      # beginnt das Füllen 
        forward(5)                                                        # zeichnet eine Raute  
        left(45)                                                            
        forward(5)                                                         
        left(135)                                                          
        forward(5)                                                         
        left(45)                                                           
        forward(5)                                                         
        right(191.2)                                                      
        n = n + 1                                                         # addiert 1 zu n und setzt das Ergebnis auf n 
        end_fill()                                                        # beendet das füllen 
        
def Pflaume():                                                            # definiert die Funktion 'Pflaume'
    begin_fill()                                                          #
    fillcolor('purple')                                                   # setzt die Füllfarbe auf Lila 
    setheading(270)                                                       # setzt Blickrichtung der Turtle nach unten
    forward(5)                                                            # zeichnet eine Raute 
    right(22.5)                                                            
    forward(10)                                                           
    left(45)                                                              
    forward(10)                                                           
    left(135)                                                             
    forward(10)                                                           
    left(45)                                                              
    forward(10)                                                           
    end_fill()                                                            # beendet das füllen

def drawLsystem(instructions,L):                                          # definiert die Funktion 'drawLsystem' welche alle Informationen für das Visualisieren des L-Systems enthält 
    savedInfoList = []                                                    # weist der Variable 'savedInfoList' eine leere Liste zu 
    for cmd in instructions:                                              # for-Schleife welche über den String 'instructions' iteriert  
        if cmd == 'A':                                                    # wenn cmd dem String 'A' entspricht geht turtle vorwärts um die Länge 'distance_1' 
            forward(L[0])
        elif cmd == 'B':                                                  # wenn cmd dem String 'B' entspricht geht turtle vorwärts um die Länge 'distance_2'
            forward(L[1])                                           
        elif cmd == 'C':                                                  # wenn cmd dem String 'C' entspricht geht turtle vorwärts um die Länge 'distance_3'
            forward(L[2])                                           
        elif cmd == 'D':                                                  # wenn cmd dem String 'D' entspricht zeichnet turtle ein Blatt 
            Blatt()                                                       
        elif cmd == 'E':                                                  # wenn cmd dem String 'E' entspricht zeichnet turtle eine Blüte
            Blüte()                                                       
        elif cmd == '+':                                                  # wenn cmd dem String '+' entspricht dreht sich turtle nach rechts
            g = gauss(L[3],L[4])                                           
            print(g)
            right(gauss(L[3],L[4])                                        # mit welchem Winkel sich die turtle nach rechts dreht hängt von dem Wert ab welche aus der Normalverteilung generiert wird                                              
        elif cmd == '-':                                                  # wenn cmd dem String '-' entspricht dreht sich turtle nach links
            h = gauss(L[5],L[6])
            print(h)                                                      
            left(gauss(L[5],L[6]))                                        # mit welchem Winkel sich die turtle nach links dreht hängt von dem Wert ab welche aus der Normalverteilung generiert wird                                             
        elif cmd == '[':                                                  # wenn cmd dem String '[' entspricht speichert turtle die aktuelle Position
            savedInfoList.append([heading(), xcor(), ycor()])             
        elif cmd == ']':                                                  # wenn cmd dem String ']' entspricht turtle geht ohne zu zeichnen zur forher gespeicherten Position und zeichnet dort weiter                                       
            newInfo = savedInfoList.pop()                                 
            setheading(newInfo[0])                                        
            up()                                                          
            setposition(newInfo[1], newInfo[2])                           
            down()                                                        