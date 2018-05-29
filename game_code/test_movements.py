
# Script 
# This script takes the robot to an rest position until waits for another order 
# Author: ABT, Juan Francisco &  DADAM, Federico
# Date: May 2018

#id 0 Motor abs_z, id=33
#id 1 Motor abs_x, id=32
#id 2 Motor abs_y, id=31
#id 3 Motor bust_y, id=34
#id 4 Motor bust_x, id=35
#id 5 Motor head_z, id=36
#id 6 Motor head_y, id=37
#id 7 Motor l_shoulder_y, id=41
#id 8 Motor l_shoulder_x, id=42
#id 9 Motor l_arm_z, id=43
#id 10 Motor l_elbow_y, id=44
#id 11 Motor r_shoulder_y, id=51
#id 12 Motor r_shoulder_x, id=52
#id 13 Motor r_arm_z, id=53
#id 14 Motor r_elbow_y, id=54


import time
from pypot.robot import from_json

from grovepi import *


bucle=True 

def electromagnet_control(electromagnet,state):
	try:
		digitalWrite(electromagnet,state)		# Send 1 to switch on the electromagnet, 0 to swtch it off
		time.sleep(1)
	except KeyboardInterrupt:
		digitalWrite(electromagnet,0)
	except IOError:
		digitalWrite(electromagnet,0)
		print ("Error")

poppy=from_json("/home/poppy/miniconda/lib/python2.7/site-packages/poppy_torso/configuration/poppy_torso_new.json")

for m in poppy.motors:
	m.compliant=False

#set grovepi+ port 4 as output

electromagnet = 4
pinMode(electromagnet,"OUTPUT")
time.sleep(1)
while(bucle):
	command = int(raw_input("Position << "))
	if (command == 0): #inicial
		motor_angles = [0,0,45,0,5,-5,0,-10,15,20,-10,-180,0,-20,0]
		mov_time = 1.5
	elif (command == 1): #inicial piezas
		motor_angles = [-25.63,-2.43,44.97,9.63,5.41,-4.25,16.8,-13.82,18.4,51.21,-76.46,-177.16,2.18,-21.14,-25.91]
		mov_time = 1.5
	elif (command == 2): #pieza1
		motor_angles = [-25.63,-2.43,44.97,9.63,5.41,-4.25,16.8,-13.82,18.4,51.21,-76.46,-127.14,3.67,-0.31,68.42]
		mov_time = 1.5
	elif (command == 3): #pieza2
		motor_angles = [-16.48,-9.55,44.0,30.37,11.65,-6.3,13.58,-28.95,14.97,51.38,-76.37,-121.69,0.07,-6.9,52.68] 
		mov_time = 1.5
	elif(command == 4): #pieza3
		motor_angles = [-13.93,7.07,42.51,17.89,0.22,-13.64,15.92,-12.15,23.76,46.64,-67.14,-134.26,-3.19,-3.38,52.07]
		mov_time = 1.5
	elif(command == 5):  #medio
		motor_angles = [23.08,-4.1,50.68,-2.86,16.57,-9.53,10.06,-4.95,11.01,-25.63,-76.81,-133.91,-1.34,17.98,45.16]
		mov_time = 1.5
	elif(command == 6): #jugada11
		motor_angles = [5.41,4.96,46.55,-14.02,-0.84,-9.53,12.11,6.4,38.26,5.14,-71.36,-168.29,3.32,12.0,50.66]
		mov_time=1.5
	elif(command == 7): #jugada12
		motor_angles = [14.2,0.74,45.85,9.8,8.13,-9.53,12.11,-13.82,24.55,13.76,-73.74,-146.13,6.4,31.34,50.13]
		mov_time = 1.5
	elif(command == 8): #jugada13
		motor_angles = [35.3,0.56,49.01,10.24,11.3,-9.53,12.11,-18.84,3.63,18.59,-76.64,-132.42,12.37,39.43,66.92]
		mov_time = 1.5
	elif(command == 9): #jugada21
                motor_angles = [10.77,7.59,65.63,-7.87,-1.89,-9.53,12.11,-11.36,11.98,36.97,-76.73,-135.41,0.86,9.8,56.55]
                mov_time = 1.5
	elif(command == 10): #jugada22
                motor_angles = [24.31,5.57,68.09,-6.37,-6.81,-9.82,12.11,-16.81,14.53,20.35,-76.55,-134.97,7.63,18.59,58.31]
                mov_time = 1.5
	elif(command == 11): #jugada23
                motor_angles = [43.82,-3.4,71.87,-9.36,-9.01,-9.53,11.82,-18.4,13.82,10.77,-76.73,-132.77,5.78,14.29,57.87]
                mov_time = 1.5
	elif(command == 12): #jugada31
                motor_angles = [25.27,5.04,84.7,-21.23,-6.11,-9.53,12.11,-50.13,19.54,23.78,-64.59,-111.32,-10.13,8.13,76.51]
                mov_time = 1.5
	elif(command == 13): #jugada32
                #motor_angles = 
                mov_time = 1.5
	elif(command == 14): #jugada33
                #motor_angles = 
                mov_time = 1.5
	elif(command == 15):  #dab
		motor_angles = [8.57,0.74,50.15,-14.81,19.82,-80.79,8.01,-92.33,98.84,-105.19,67.36,-95.32,12.81,77.23,-3.58]
		mov_time = 1.5
	elif (command == 98): #saludo
		motor_angles = [5.41,-5.51,75.74,-26.95,12.35,-4.25,0.67,-0.2,10.31,-20.0,-76.55,-102.97,4.55,17.98,68.24]
		mov_time=1.5
	elif (command == 99):
		electromagnet_control(electromagnet,1)
	elif (command == 100):
		electromagnet_control(electromagnet,0)
	elif(command == 69):
		bucle=False

	elif(command == -1):
		print poppy.motors

	elif(command == -2):
		for m in poppy.motors:
			m.compliant=True

	elif(command == -3): 
		for m in poppy.motors:
			m.compliant=False

	elif(command == -4):
		poppy.motors[11].compliant=True
		poppy.motors[12].compliant=True
		poppy.motors[13].compliant=True
		poppy.motors[14].compliant=True
	else:
		print "Wrong command, setting initial position"
		motor_angles = [0,0,45,0,5,-5,0,10,15,20,-10,-180,0,-20,0]
		mov_time = 2
	if(bucle):
		poppy.motors[0].goto_position(motor_angles[0],mov_time)
		poppy.motors[1].goto_position(motor_angles[1],mov_time)
		poppy.motors[2].goto_position(motor_angles[2],mov_time)
		poppy.motors[3].goto_position(motor_angles[3],mov_time)
		poppy.motors[4].goto_position(motor_angles[4],mov_time)
		poppy.motors[5].goto_position(motor_angles[5],mov_time)
		poppy.motors[6].goto_position(motor_angles[6],mov_time)
		poppy.motors[7].goto_position(motor_angles[7],mov_time)
		poppy.motors[8].goto_position(motor_angles[8],mov_time)
		poppy.motors[9].goto_position(motor_angles[9],mov_time)
		poppy.motors[10].goto_position(motor_angles[10],mov_time)
		poppy.motors[11].goto_position(motor_angles[11],mov_time)
		poppy.motors[12].goto_position(motor_angles[12],mov_time)
		poppy.motors[13].goto_position(motor_angles[13],mov_time)
		poppy.motors[14].goto_position(motor_angles[14],mov_time)
		time.sleep(1.5)
	
