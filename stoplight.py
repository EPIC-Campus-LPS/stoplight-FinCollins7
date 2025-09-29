import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#setup for the first light
GPIO.setup(18, GPIO.OUT)
print("Green LED on")
GPIO.output(18,GPIO.HIGH)
#turn on led
time.sleep(4)
#keep on for 4 seconds
print("Green LED off")
GPIO.output(18,GPIO.LOW)
#turn off led
GPIO.setup(19,GPIO.OUT)
#setup for yellow light
print("Yellow LED on")
GPIO.output(19,GPIO.HIGH)
#turn on yellow
time.sleep(1)
#keep on for 1 second
print("Yellow LED off")
GPIO.output(19,GPIO.LOW)
#yellow led off
GPIO.setup(20, GPIO.OUT)
#setup for red
print("Red LED on")
GPIO.output(20,GPIO.HIGH)
#red led on
time.sleep(5)
#red led on for 5 seconds
print("Red LED off")
GPIO.output(20,GPIO.LOW)
#red led off
