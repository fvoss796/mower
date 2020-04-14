# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:38:09 2019

@author: Fabian Voß
"""
import RPi.GPIO as GPIO
import time


linksVW = 21
linksRW = 20

"""
linker Motor: 20, --21--,16 PWM: 16
rechter Motor: --26--,19,13 PWM:13
"""
class Fahren:
    def __init__(self):
            global pwmLinks
            global pwmRechts
            #links
            GPIO.setup(20, GPIO.OUT)
            GPIO.setup(21, GPIO.OUT)
            GPIO.setup(16, GPIO.OUT)
            #rechts
            GPIO.setup(26, GPIO.OUT)
            GPIO.setup(19, GPIO.OUT)
            GPIO.setup(13, GPIO.OUT)
            #pwmRechts=GPIO.PWM(13,100)
            #pwmLinks = GPIO.PWM(16, 100)
            #pwmLinks.start(0)
            #pwmRechts.start(0)
            GPIO.output(20, False)
            GPIO.output(21, True)
            GPIO.output(26,True)
            GPIO.output(19,False)
    def geradeaus(self,speed):
            #pwmLinks.ChangeDutyCycle(10)
            GPIO.output(26, True)
            GPIO.output(21, True)
    def rueckwaerts(self, speed):
            print("REVERSE")
            GPIO.output(19, True)
            GPIO.output(20, True)
    def stop(self):
            GPIO.output(21,False)
            GPIO.output(26, False)
            GPIO.output(19, False)
            GPIO.output(20, False)
    def linksDrehen(self, degree):
            print("DREHE LINKS")
            GPIO.output(19, True)
            time.sleep(degree/10)
            GPIO.output(19, False)
    def rechtsDrehen(self, degree):
            print("DREHE RECHTS")
            GPIO.output(20, True)
            time.sleep(degree/10)
            GPIO.output(20, False)
    def leichtLinksDrehen(self, degree):
            print("DREHE LEICHT LINKS")
            GPIO.output(21, True)
            time.sleep(degree/10)
            GPIO.output(21, False)
    def leichtRechtsDrehen(self, degree):
            print("DREHE LEICHT RECHTS")
            GPIO.output(26, True)
            time.sleep(degree/10)
            GPIO.output(26, False)
