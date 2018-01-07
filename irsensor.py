import serial
import time
import Rpi.GPIO as GPIO
from rfid import readrfid
	from fire import locat
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.IN)
	GPIO.setup(12,GPIO.IN)
	GPIO.setup(13,GPIO.IN)
	GPIO.setup(15,GPIO.IN)
	GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.IN)
	while True:
	loc1= GPIO.input(11)
	loc2= GPIO.input(12)
	plant1= GPIO.input(13)
	plant2= GPIO.input(15)
	customer= GPIO.input(16)
park= GPIO.input(18)
	if plant1 == True:
	print(“Parcel has reached plant 1”)x=”a”
	y=readrfid()
	locat(x,y)
time.sleep(1)
	elif plant2 == True:
print(“Parcel has reached plant 2”)
	x=”b”
	y=readrfid()
	locat(x,y)
time.sleep(1)
	elif loc1 == True:
print(“Parcel has reached location 1”)
	x=”c”
	y=readrfid()
	locat(x,y)
time.sleep(1)
	elif loc2 == True:
print(“Parcel has reached location 2”)
	x=”d”
	y=readrfid()
	locat(x,y)
time.sleep(1)
	elif customer == True:print(“Parcel has reached customer”)
	x=”e”
	y=readrfid()
	locat(x,y)
time.sleep(1)
	else:
	print(“”)
time.sleep(1)
