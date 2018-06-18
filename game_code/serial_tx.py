import time
import serial

#print 'Enter serial port number:\r'
#1serial_port = raw_input("<< ")
#ser.port = 'COM' + serial_port,
#ser.isOpen()

ptr = 0
for ptr in range (0,32):
	try:
		ser = serial.Serial()
		ser.port = '/dev/ttyS' + str(ptr)
		ser.baudrate=9600
		ser.parity=serial.PARITY_NONE
		ser.stopbits=serial.STOPBITS_ONE
		ser.bytesize=serial.EIGHTBITS
		ser.timeout = 1
		ser.open()
		print ("Port"+ str(ptr)+ "has been opened")
	except Exception, e:
	    print ("error open serial port: " + str(ptr) + " ") + str(e)
	    #exit()

delay = 0.002*5

while 1:
	print 'Enter data:\r'
	data = raw_input("<< ")
	if data == 'exit':
		ser.close()
		exit()
	else:
		ser.write(data)
		time.sleep(delay)