# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:38:09 2019

@author: Fabian Voß
"""
import RPi.GPIO as GPIO
import random
import time
from fahren import Fahren
from messen import Messen
from maehen import Maehen
from chart import Chart
chart = Chart()
center = Messen(22,23)
left = Messen(18,27)
right = Messen(24,25)
fahren = Fahren()
maehen = Maehen()
minDistance = 30
loopSpeed = 0.7
loopsTilChange = 15
currentLoop = 0
myList = []

def checkDistance():
    myList = []
    tmp = left.messen()
    myList.append(tmp)
    #logging
    chart.log(str(tmp)+" ")
    time.sleep(0.2)
    tmp = center.messen()
    myList.append(tmp)
    #logging
    chart.log(str(tmp)+" ")
    time.sleep(0.2)
    tmp = right.messen()
    myList.append(tmp)
    #logging
    chart.log(str(tmp)+"\n")
    print(myList)
    print("--------------------- "+str(int(min(myList))))
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
        #Schaue, ob irgendwo zu eng
        aktuelleDistanz = checkDistance()
        if(aktuelleDistanz < minDistance):
                currentLoop = 0
                #Zu eng irgendwo
                chart.log("0 0 0\n")
                fahren.stop()
                maehen.ausschalten()
                if(aktuelleDistanz < 10):
                    chart.log("-20 -20 -20\n")
                    #Viel zu eng, kurzfristig ein Objekt gefunden. Erst zurück fahren
                    fahren.rueckwaerts(100)
                    while(checkDistance() < minDistance):
                            time.sleep(loopSpeed)
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
                time.sleep(loopSpeed)
        #Checke, ob wir wieder zufällig drehen sollen
        if(currentLoop>loopsTilChange):
            fahren.stop()
            if(bool(random.getrandbits(1))):
                fahren.leichtLinksDrehen(30)
                chart.log("-20 0 0 \n")
            else:
                fahren.leichtRechtsDrehen(30)
                chart.log("0 0 -20 \n")
            currentLoop = 0
        currentLoop += 1

except KeyboardInterrupt:
    print("Abbruch")
    GPIO.cleanup()
