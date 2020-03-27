# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:38:09 2019

@author: Fabian Voß
"""
import RPi.GPIO as GPIO
import time
from fahren import Fahren
from messen import Messen
from maehen import Maehen
center = Messen(22,23)
left = Messen(18,27)
right = Messen(24,25)
fahren = Fahren()
maehen = Maehen()
myList = []

def checkDistance():
    myList = []
    myList.append(left.messen())
    time.sleep(0.2)
    myList.append(center.messen())
    time.sleep(0.2)
    myList.append(right.messen())
    print(myList)
    print("---------------"+str(int(min(myList))))
    return(int(min(myList)))
def checkSite():
    l = left.messen()
    time.sleep(0.2)
    c = center.messen()
    time.sleep(0.2)
    r = right.messen()
    if(r < c and r < l):
        return("r")
        print("rechts eng")
    if(c < r and c < l):
        return("c")
        print("vorne eng")
    if(l < c and l < r):
        return("l")
        print("links eng")

try:
    while(True):
        time.sleep(1.0)
        if(checkDistance() < 20):
                #Zu end irgendwo, fahre rückwärts bis genug Platz
                fahren.stop()
                maehen.ausschalten()
                fahren.rueckwaerts(100)
                while(checkDistance() < 40):
                        time.sleep(1.0)
                fahren.stop()
                #Überprüfe, wo am meisten PLatz ist
                if(checkSite() == "r"):
                    #drehe links
                    fahren.linksDrehen(90)
                else:
                    #drehe rechts
                    fahren.rechtsDrehen(90)
        else:
                fahren.geradeaus(100)
                maehen.einschalten()

except KeyboardInterrupt:
    print("Abbruch")
    GPIO.cleanup()
