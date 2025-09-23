import RPi.GPIO as GPIO
import time
from gpiozero import Button
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
from gpiozero import Button
from signal import pause
def touched():
	print("Touched!")
	GPIO.setup(18,GPIO.OUT)
	print("Green LED on")
	GPIO.output(18,GPIO.HIGH)
	time.sleep(4)
	print("Green LED off")
	GPIO.output(18,GPIO.LOW)
	GPIO.setup(19,GPIO.OUT)
	print("Yellow LED on")
	GPIO.output(19,GPIO.HIGH)
	time.sleep(1)
	print("Yellow LED off")
	GPIO.output(19,GPIO.LOW)
	GPIO.setup(20, GPIO.OUT)
	print("Red LED on")
	GPIO.output(20,GPIO.HIGH)
	time.sleep(5)
	print("Red LED off")
	GPIO.output(20,GPIO.LOW)
def not_touched():
	print("Not Touched!")

touch_sensor = Button(21, pull_up=None, active_state=True)
touch_sensor.when_pressed = touched
touch_sensor.when_released = not_touched

pause()
