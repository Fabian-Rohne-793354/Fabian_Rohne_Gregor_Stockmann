# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:19:09 2018

@author: xReinheitsgebotx
"""

from random import *                                      # importiert alles aus dem Modul random   

def processString(n, oldString):                          # definiert eine Funktion 'processString' mit den Argumenten 'n' (int) und 'oldString' (str)
    newString = ""                                        # weist der lokalen Variable 'newString' einen leeren String   
    for ch in oldString:                                  # for loop der über den in processString eingegebenen String iteriert 
        newString = newString + applyRules(n, ch)         # weist newString die Additon des Ergebnisses der Definiton applyRules mit sich selbst zu 
        
    return newString                                      # gibt newString als Ergebnis der Funktion aus   

def applyRules(n, ch):                                    # definiert eine Funktion 'applyRules' mit den Argumenten 'n' (int) und 'ch' (str)  
    newString = ""                                        # weist der lokalen Variable 'newString' einen leeren String  
    if ch == "A":                                         # wenn der in die Funktion eigegebene String 'ch' dem String 'A' entspricht führe folgende Anweisungen aus  
        newString = '[-B-C][+B+C]'                        # wendet die Regel A>[-B-C][+B+C] an    
        if n > 1:                                         # wenn der in die Funktion eigegebene Integer 'n' größer 0 ist führe folgende Anweisungen aus 
            n = n - 1                                     # subtrahiert 1 von 'n'     
            newString = processString(n, newString)       # weist der lokalen Variable 'newString' das Resultat der Funktion 'processString' mit den Argumenten 'n' (int) und 'newString' (str)     
            newString = "A" + newString                   # Addiert den int 'A' zu der Variable 'newString'  
        else: newString = "A" + newString                 # wenn die if Bedingung nicht erfüllt ist wird der int 'A' zu der lokalen Variable 'newString' addiert
    elif ch == "B":                                       # wenn der in die Funktion eigegebene String 'ch' dem String 'B' entspricht führe folgende Anweisungen aus  
        x = random()                                      # weist x einen zufälligen float zwischen Null und Eins zu   
        print(x)                                          # gibt die Variable 'x' in der Console aus   
        if x < 0.25:                                      # wenn die Variable 'x' kleiner als 0.25 ist wende die Regel B>[+B-B] an      
            newString = '[+B-B]'                            
        elif x < 0.5:                                     # wenn die Variable 'x' kleiner als 0.5 ist wende die Regel B>[-B+B] an     
            newString = '[-B+B]'                            
        elif x < 0.7:                                     # wenn die Variable 'x' kleiner als 0.7 ist wende die Regel B>[+B+C+C] an 
            newString = '[+B+C+C]'                          
        elif x < 0.9:                                     # wenn die Variable 'x' kleiner als 0.9 ist wende die Regel B>[-B-C-C] an  
            newString = '[-B-C-C]'                         
        elif x < 1.0:                                     # wenn die Variable 'x' kleiner als 1.0 ist wende die Regel B>[-C+C] an  
            newString = '[-C+C]'                            
        if n > 1:                                         # wenn der in die Funktion eigegebene Integer 'n' größer 0 ist führt folgende Anweisungen aus      
            n = n - 1                                     # subtrahiert 1 von 'n' 
            newString = processString(n, newString)       # weist der lokalen Variable 'newString' das Resultat der Funktion 'processString' mit den Argumenten 'n' (int) und 'newString' (str)     
            newString = "B" + newString                   # Addiert den int 'B' zu der Variable 'newString'     
        else: newString = "B" + newString                 # wenn die if Bedingung nicht erfüllt ist wird der int 'B' zu der lokalen Variable 'newString' addiert
    elif ch == "C":                                       # wenn der in die Funktion eigegebene String 'ch' dem String 'C' entspricht führe folgende Anweisungen aus      
       x = random()                                       # weist x einen zufälligen float zwischen Null und Eins zu
       print(x)                                           # gibt die Variable 'x' in der Console aus
       if x < 0.25:                                       # wenn die Variable 'x' kleiner als 0.25 ist wende die Regel C>[-C+C+D]
           newString = '[-C+C+D]'
       elif x < 0.5:                                      # wenn die Variable 'x' kleiner als 0.5 ist wende die Regel C>[+C-C-D]
           newString = '[+C-C-D]'
       elif x < 0.7:                                      # wenn die Variable 'x' kleiner als 0.7 ist wende die Regel C>[-C-D]
           newString = '[-C-D]'
       elif x < 0.9:                                      # wenn die Variable 'x' kleiner als 0.9 ist wende die Regel C>[+C+D]
           newString = '[+C+D]'
       elif x < 0.95:                                     # wenn die Variable 'x' kleiner als 0.95 ist wende die Regel C>[-C+E]
           newString = '[-C+E]'
       elif x < 1.0:                                      # wenn die Variable 'x' kleiner als 1.0 ist wende die Regel C>[+C-E]
           newString = '[+C-E]'                           #
       if n > 1:                                          # wenn der in die Funktion eigegebene Integer 'n' größer 0 ist führt folgende Anweisungen aus
           n = n - 1                                      # subtrahiert 1 von 'n'
           newString = processString(n, newString)        # weist der lokalen Variable 'newString' das Resultat der Funktion 'processString' mit den Argumenten 'n' (int) und 'newString' (str)
           newString = "C" + newString                    # Addiert den int 'C' zu der Variable 'newString'
       else: newString = "C" + newString                  # wenn die if Bedingung nicht erfüllt ist wird der int 'C' zu der lokalen Variable 'newString' addiert
    else:                                                 # wenn ch weder dem int 'A' noch 'B' noch 'C' entspricht setze 'newString' auf ch
        newString = ch                                    
    
    return newString                                      # gibt newString als Ergebnis der Funktion aus 