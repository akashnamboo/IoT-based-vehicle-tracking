import serial
def readrfid():
	Ser=serial.Serial(”/dev/ttyAMA0”)
	ser.baudrate=9600
	data=ser.read(12)
	ser.close()
	return data
	id=readrfid()
	print(id)
