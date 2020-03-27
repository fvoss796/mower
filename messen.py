# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:38:09 2019

@author: Fabian Voß
"""
import RPi.GPIO as GPIO
import time
class Messen:
    def __init__(self, trigger, echo):
            self.GPIO_TRIGGER = trigger
            self.GPIO_ECHO = echo
            GPIO.setmode(GPIO.BCM)
            print(self.GPIO_TRIGGER,self.GPIO_ECHO)
            #Richtung der GPIO-Pins festlegen (IN / OUT)
            GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
            GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def messen(self):
            # setze Trigger auf HIGH
            GPIO.output(self.GPIO_TRIGGER, True)

            # setze Trigger nach 0.01ms auf LOW
            time.sleep(0.00001)
            GPIO.output(self.GPIO_TRIGGER, False)

            StartZeit = time.time()
            StopZeit = time.time()

            # speichere Startzeit
            while GPIO.input(self.GPIO_ECHO) == 0:
                StartZeit = time.time()

            # speichere Ankunftszeit
            while GPIO.input(self.GPIO_ECHO) == 1:
                StopZeit = time.time()

            # Zeit Differenz zwischen Start und Ankunft
            TimeElapsed = StopZeit - StartZeit
            # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
            # und durch 2 teilen, da hin und zurueck
            distanz = (TimeElapsed * 34300) / 2
            print(distanz)
            return(distanz)
