# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:24:06 2018

@author: xReinheitsgebotx
"""
from Lsystem import *                           # importiert das Modul welches den String des L-Systems generiert 
from turtle_baum import *                       # importiert das Modul welches das L-System mittels turtle graphics visualisiert
from tkinter import * 

def main(n,d_1,d_2,d_3,x,y):                # definiert die Funktion 'main'
    inst = processString(n, "[A]")                # greift auf eine Funktion des Moduls L-System zu um den String für das L-System zu generieren
    print(inst)                                 # gibt den String des L-Systems in der Konsole aus 
    
    penup()                                     # Turtle hört auf zu zeichnen 
    goto(0,-250)                                # Startposition der Turtel
    left(90)
    pendown()                                   # Turtle fängt an zu zeichnen 
    speed(0)                                    # Geschwindigkeit
    drawLsystem(inst,d_1,d_2,d_3,x,y)       # greift auf eine Funktion des Moduls 'turtle_baum' um den generierten String zu zeichnen
    ts = getscreen()                            # weist der Variable 'ts' das Objekt zu welches Turtle gezeichnet hat 
    ts.getcanvas().postscript(file="tree.eps")  # speichert das gezeichnete Objekt als Vektiorgrafik
    done()                                      # Turtle ist fertig mit zeichnen
                          
    exitonclick()                               # Turtle Graphics kann durch Mausklick beendet werden 

main(8,                                         # ruft die Funktion main auf
     30,
     20,
     10,
     gauss(25,20),
     gauss(25,20)
    )                             