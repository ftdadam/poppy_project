import time
import serial

print 'Enter serial port number:\r'
serial_port = raw_input("<< ")
if(serial_port != '' ):
	ser = serial.Serial(
	    port = 'COM' + serial_port,
	    #port='COM4',	#Configurar con el puerto
	    baudrate=9600,
	    parity=serial.PARITY_NONE,
	    stopbits=serial.STOPBITS_ONE,
	    bytesize=serial.EIGHTBITS
	)
	ser.isOpen()
	ser.timeout = 1
	print 'Communication Established\n'
	#print(ser.timeout)
else:
	print 'Communication Override\n'

delay = 0.002*5

while 1:
	data = ser.read()
	if(data.__len__ > 0 ):
		print data
		if(data == 'x'):
			ser.close()
			exit()