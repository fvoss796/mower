# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:38:09 2019

@author: Fabian Voß
"""
import RPi.GPIO as GPIO
import time
class Maehen:
    def __init__(self):
        GPIO.setup(4, GPIO.OUT)
        GPIO.output(4, True)

    def einschalten(self):
        GPIO.output(4, False)
    def ausschalten(self):
        GPIO.output(4, True)
