# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:38:09 2019

@author: Fabian Voß
"""
f = open("distance.txt","w+")
class Chart:
    def __init__(self):
        f.write("+++++++++++++ Starten des Loggings +++++++++++++++++++\n")
        f.write("l c r\n")
    def log(self, text):
        f.write(text)
    def close(self):
        f.close()
