#!/usr/bin/env python
import os

#Python 2.7 / On Script

#Libraries
import RPi.GPIO as GPIO
import time

# Pin setup
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# Pin ON
GPIO.output(17,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
