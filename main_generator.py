# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:50:44 2018

@author: xReinheitsgebotx
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:24:06 2018

@author: xReinheitsgebotx
"""
from Lsystem import *                            # importiert das Modul welches den String des L-Systems generiert 
from turtle_baum import *                        # importiert das Modul welches das L-System mittels turtle graphics visualisiert
from tkinter import * 

def main(n,d_1,d_2,d_3,a_1,a_2):                 # definiert die Funktion 'main'
    inst = processString(n, "[A]")               # greift auf eine Funktion des Moduls L-System zu um den String für das L-System zu generieren
    print(inst)                                  # gibt den String des L-Systems in der Konsole aus 

    drawLsystem(inst,d_1,d_2,d_3,a_1,a_2)        # greift auf eine Funktion des Moduls 'turtle_baum' um den generierten String zu zeichnen
    ht()                                         # Turtle wird unsichtbar 
                  

def main_generator(a,                            # a entspricht der Anzahl an Bäumen die gezeichnet werden 
                   n,                            # Anzahl der  
                   d_1,d_2,d_3,a_1,a_2,          # Aste und Winkel 
                   b):                           # b Ordner in dem die Bilder der Bäume gespeichert werden                  
    penup()                                      # Turtle hört auf zu zeichnen 
    goto(0,-250)                                 # Startposition der Turtel
    setheading(90)
    pendown()                                    # Turtle fängt an zu zeichnen 
    speed(0)                                     # Geschwindigkeit
    i = 1                                        # weist i den Integer 1 zu
    while i <= a:                                # Schleife läuft solange wie i kleiner gleich a ist 
        main(n,d_1,d_2,d_3,a_1,a_2)              # ruft die Funktion main auf
        ts = getscreen()                         # weist der Variable 'ts' das Objekt zu welches Turtle gezeichnet hat 
        y = b + '/' + str(i) + 'tree.eps'        # ändert den Namen der Datei nach jedem durchgang so das alte Dateien nicht überschrieben werden 
        ts.getcanvas().postscript(file=y)        # speichert das gezeichnete Objekt als Vektiorgrafik
        clear()                                  # löscht das Objekt aus dem Turtlescreen 
        i += 1                                   # addiert 1 zu i und setzt das Ergebnis auf i  
                                                 # solte die while Schleife False sein schließt Pyhton turtle    
           
# main_generator(10,8)                             # ruft die Funktion main_generator auf 

#main_generator(1,8,60,40,20,gauss(25,1),gauss(25,1),"gen_tree(1,8,60,40,20,gauss(25,1),gauss(25,1))")

#main_generator(1,8,60,40,20,gauss(25,5),gauss(25,5),"gen_tree(1,8,60,40,20,gauss(25,5),gauss(25,5))")

#main_generator(1,8,60,40,20,gauss(25,10),gauss(25,10),"gen_tree(1,8,60,40,20,gauss(25,10),gauss(25,10))")

main_generator(1,8,60,40,20,gauss(15,1),gauss(15,1),"gen_tree(20,8,60,40,20,gauss(25,20),gauss(25,20))")
      
bye()