import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
time.sleep(0.1)
Pin = 18
def photocell(Pin):
	detect = 0
	time.sleep(.05)
	GPIO.setup(Pin, GPIO.IN)
	while(GPIO.input(18) == GPIO.LOW):
		detect += 1
		if detect > 5000:
			break
	return(detect)

try:
	dark_threshold = 1000
	while True:
		detect = photocell(18)
		if detect > dark_threshold:
	#print("LEDs on")
			GPIO.output(19,GPIO.HIGH)
			GPIO.output(20,GPIO.HIGH)
			GPIO.output(21,GPIO.HIGH)


		elif detect == 0:
			GPIO.output(19,GPIO.LOW)
			GPIO.output(20,GPIO.LOW)
			GPIO.output(21,GPIO.LOW)
	#print("Light!")
except KeyboardInterrupt:
	GPIO.cleanup()
