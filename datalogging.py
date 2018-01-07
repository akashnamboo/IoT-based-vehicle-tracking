import RPi.GPIO as GPIO
import time
import httplib, urllib
import socket
import serial
server= “data.sparkfun.com”
publicKey= “VGX6Jn9A15INybNybHYOJ3Z”
privateKey= “9Yglm8pAwzhA76wypoD1”
fields= [“location”,”rfid”,”timestamp”]
try:
def locat(loc, rfid):
	print(“Here we go! Press Ctrl+C to exit”)
	print(“Sending an update!”)
	data={}
	data[fields[0]] = location
	data[fields[1]] = rfid
	data[fields[2]] = time.strftime(“%A %B %d, %Y %H:%M:%S”)
params = urllib.urlencode(data)
	headers={}
	headers[“Content-Type”] = ”application/x-www-form-urlencoded”headers[“Connection”] = ”close”
headers[“Content-Length”] = len(params)
	headers[“Phant-Private-Key”] = privateKey
	c = httplib.HTTPConnection(server)
	c.request(“POST”, “/input/” + “.txt”, params, headers)
r = c.getresponse()
	print r.status, r.reason
time.sleep()
	except KeyboardInterrupt:
GPIO.cleanup()
