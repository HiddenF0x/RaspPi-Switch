#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################
## This script kills the "strobe" script  ##
############################################


# Libraries
import RPi.GPIO as GPIO # Used to reset GPIO
import os
import sys
import signal
import time

# Clear Active Pins
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# Read PID from pid.txt
f=open("pid.txt", "r")
lines = f.readlines()  # return a list of lines in file
list_of_elements = []
for line in lines:
    list_of_elements += line.split()
    f.close()
print list_of_elements[0]
PID = int(list_of_elements[0])
os.kill(PID, signal.SIGTERM) #or signal.SIGKILL
GPIO.output(17,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(0.1)
sys.exit
