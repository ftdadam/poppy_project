
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
	elif (command == 2):
		motor_angles = [-25.63,-2.43,44.97,9.63,5.41,-4.25,16.8,-13.82,18.4,51.21,-76.46,-127.14,3.67,-0.31,68.42]
		mov_time = 1.5
	elif (command == 3): 
		motor_angles = [-18.68, 3.99, 52.35, -2.59, 4.7, -5.13, 16.51, -13.82, 18.4, 51.21, -76.46, -150.7, -3.27, -0.84, 40.7] 
		mov_time = 1.5
	elif(command == 4):  #medio
		motor_angles = [23.08,-4.1,50.68,-2.86,16.57,-9.53,10.06,-4.95,11.01,-25.63,-76.81,-133.91,-1.34,17.98,49.16]
		mov_time = 1.5
	elif(command == 5):  #dab
		motor_angles = [8.57,0.74,50.15,-14.81,19.82,-80.79,8.01,-92.33,98.84,-105.19,67.36,-95.32,12.81,77.23,-3.58]
		mov_time = 1.5
	elif(command == 6):  #agarrar 
		motor_angles = [-25.63,-2.43,44.97,9.63,5.41,-4.25,16.8,-13.82,18.4,51.21,-76.46,-127.14,3.67,-0.31,68.42]
		mov_time = 1.5
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
	
