import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)