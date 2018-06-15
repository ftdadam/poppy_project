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
	print 'Enter data:\r'
	data = raw_input("<< ")
	if data == 'exit':
	    if(serial_port != '' ):
	    	ser.close()
	    exit()
	else:
		ser.write(chr(data))
		time.sleep(delay)