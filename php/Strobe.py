#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Libraries
import os
import sys
import argparse # Arguments (-t -s)
#import RPi.GPIO as GPIO # Control "api" for raspberry pi
import time # Used for speed and rate clock.

# Setup inputs
def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Backend script used for RaspberryPi-Switch strobe')
    # Add arguments
    parser.add_argument(
        '-t', '--time', type=int, help='Time Script is active in seconds', required=True)
    parser.add_argument(
        '-s', '--speed', type=float, help='Time of delay between toggle on off.', required=True,)
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    clock = args.time
    speed = args.speed
    # Return all variable values
    return clock, speed

# Pin setup
##GPIO.setwarnings(False)
##GPIO.cleanup()
##GPIO.setmode(GPIO.BCM)
##GPIO.setup(17,GPIO.OUT)
##GPIO.setup(18,GPIO.OUT)
# Setup PID.txt
#function Check_PID():
f= open("pid.txt", "w+")
PID = os.getpid()
print (str(PID))
f.write(str(PID))
f.close()
# Start script
clock, speed = get_args()
# Prints variables
print "\nTime remaining: [ %s ]\n" % clock
print "\nStrobe rate: [ %s ]\n" % speed
# Check_PID()
# Actual loop
t_end = time.time() + clock
while time.time() < t_end:
    #GPIO.output(17,GPIO.LOW)
    #GPIO.output(18,GPIO.LOW)
    print('on')
    time.sleep(float(speed))
    print('off')
    #GPIO.output(17,GPIO.HIGH)
    #GPIO.output(18,GPIO.HIGH)
    time.sleep(float(speed))
sys.exit()
