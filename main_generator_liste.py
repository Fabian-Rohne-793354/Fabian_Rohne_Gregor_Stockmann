# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:16:41 2018

@author: xReinheitsgebotx

Wichtig

Die Dateien Lsystem.py und turtle_baum_liste.py zu den gleichnamigen Modulen müssen sich im geleichen Ordner befinden.  
"""

from Lsystem import *                            # importiert das Modul welches den String des L-Systems generiert 
from turtle_baum_liste import *                  # importiert das Modul welches das L-System mittels turtle graphics visualisiert
from tkinter import                              # importiert das Modul 'tkinter'
import os                                        # importiert das Modul 'os'

def main(n,L):                                   # definiert die Funktion 'main'
    inst = processString(n, "[A]")               # greift auf eine Funktion des Moduls L-System zu um den String für das L-System zu generieren
    print(inst)                                  # gibt den String des L-Systems in der Konsole aus 

    drawLsystem(inst,L)                          # greift auf eine Funktion des Moduls 'turtle_baum' um den generierten String zu zeichnen
    ht()                                         # Turtle wird unsichtbar 
                  

def main_generator(l):                           # definiert die Funktion 'main_generator' welche eine Liste 'l' als Argument                    
    os.makedirs(l[3],exist_ok=True)              # erstelt einen Ordner mit dem in der Liste gespeicherten Namen solange noch kein Ordner mit dem Namen existiert
    penup()                                      # Turtle hört auf zu zeichnen 
    goto(0,-250)                                 # Startposition der Turtel
    setheading(90)
    pendown()                                    # Turtle fängt an zu zeichnen 
    speed(0)                                     # Geschwindigkeit
    i = 1                                        # weist i den Integer 1 zu
    while i <= l[0]:                             # Schleife läuft solange wie i kleiner gleich a ist 
        main(l[1],l[2])                          # ruft die Funktion main auf
        ts = getscreen()                         # weist der Variable 'ts' das Objekt zu welches Turtle gezeichnet hat 
        z = l[3] + '/' + str(i) + 'tree.eps'     # ändert den Namen der Datei nach jedem durchgang so das alte Dateien nicht überschrieben werden 
        ts.getcanvas().postscript(file=z)        # speichert das gezeichnete Objekt als Vektorgrafik
        clear()                                  # löscht das Objekt aus dem Turtlescreen 
        i += 1                                   # addiert 1 zu i und setzt das Ergebnis auf i  

"""
Erklärung der Funktion main_generator

l[0] : int der bestimmt wie viele Bäume generiert werden sollen

l[1] : int der bestimmte wie viele Ebenen die Bäume haben

l[2] : list welche die Gestalt des Baumes bestimmt [Länge Stamm, Länge großer Ast, Länge kleiner Ast,
       Erwartungswert bei Drehung nach Rechts, Standardabweichung bei Drehung nach Rechts,
       Erwartungswert bei Drehung nach Links, Standardabweichung bei Drehung nach Links]   

l[3] : str der den Namen des Ordners angibt in welchem die Bilder der generierten Bäume gespeichert werden   
"""
main_generator([100,8,[60,40,20,12,1,18,1],"gen_tree(100,8,[60,40,20,12,1,18,1])"])

main_generator([100,8,[60,40,20,12,2.5,18,2,5],"gen_tree(100,8,[60,40,20,12,2.5,18,2,5])"])

main_generator([100,8,[60,40,20,12,5,18,5],"gen_tree(100,8,[60,40,20,12,5,18,5])"])

main_generator([100,8,[60,40,20,15,10,18,10],"gen_tree(100,8,[60,40,20,12,10,18,10])"])
      
bye()

"""
