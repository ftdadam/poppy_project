
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
		digitalWrite(electromagnet,state)	# 1: Switch on
							# 0 to swtch it off
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
		motor_angles = [-25.89, -3.66, 45.32, 10.15, 4.09, -5.13, 16.22, -14.18, 17.87, 51.38, -76.11, -169.96, 4.81, 4.26, -54.84]
		mov_time = 1.5
	elif (command == 2): #pieza1
		motor_angles = [-25.71, -4.63, 45.23, 10.51, 3.47, -6.6, 12.7, -14.09, 17.6, 51.65, -49.91, -160.46, 9.65, -4.18, 30.18]
		mov_time = 1.5
	elif (command == 3): #pieza2
		motor_angles = [-32.57, 0.65, 39.69, 20.26, -5.32, -4.25, 15.92, -15.14, 21.65, 49.1, -76.9, -150.79, 12.2, 6.11, 35.45]
		mov_time = 1.5
	elif(command == 4): #pieza3
		motor_angles = [-25.98, 0.12, 33.1, 18.07, 0.13, -4.25, 15.34, -12.95, 17.96, 49.36, -76.73, -154.84, 2.7, 8.31, 38.97]
		mov_time = 1.5
	elif(command == 5): #pieza4
		motor_angles = [-11.47, 6.01, 37.93, 13.76, -7.43, -4.25, 15.92, -21.47, 25.16, 33.63, -69.6, -169.6, 4.73, -2.24, 29.56]
		mov_time = 1.5
	elif(command == 6): #pieza5
		motor_angles = [-18.59, 1.09, 36.97, 16.92, 3.21, -4.25, 15.92, -9.08, 12.15, 27.47, -74.79, -159.58, -4.15, 10.59, 37.21]
		mov_time = 1.5
	elif(command == 7):  #medio
		motor_angles = [23.08,-4.1,50.68,-2.86,16.57,-9.53,10.06,-4.95,11.01,-25.63,-76.81,-133.91,-1.34,17.98,45.16]
		mov_time = 1.5
	elif(command == 8): #jugada11
		motor_angles = [23.16, -4.89, 50.95, -3.03, 15.34, -5.43, 10.35, -5.21, 11.36, -25.54, -76.46, -189.12, -5.47, -4.44, 6.09]
		mov_time=1.5
	elif(command == 9): #jugada12
		motor_angles = [22.81, -4.8, 50.86, -3.12, 15.69, -5.43, 10.06, -5.21, 11.36, -25.54, -76.46, -165.38, -10.92, 41.8, 21.91]
		mov_time = 1.5
	elif(command == 10): #jugada13
		motor_angles = [35.82, -11.57, 47.78, -5.32, 16.75, -5.43, 10.06, -11.45, 9.43, -12.7, -74.53, -150.09, 9.56, 32.04, 51.19]
		mov_time = 1.5
	elif(command == 11): #jugada21
                motor_angles = [7.43, -11.13, 48.31, -2.07, 25.54, -5.43, 10.06, -6.18, 1.87, -5.58, -74.88, -138.13, -8.02, 10.51, 60.15]
                mov_time = 1.5
	elif(command == 12): #jugada22
                motor_angles = [16.66, -11.04, 48.4, -5.23, 25.01, -5.43, 10.06, -5.47, 2.48, 0.04, -74.79, -137.16, 1.21, 20.35, 64.64]
                mov_time = 1.5
	elif(command == 13): #jugada23
                motor_angles = [32.22, -20.8, 56.4, -8.13, 25.54, -5.43, 10.06, -15.49, 4.07, -12.35, -74.88, -125.38, 5.08, 24.31, 64.2]
                mov_time = 1.5
	elif(command == 14): #jugada31
                motor_angles = [13.58, -13.07, 70.99, -1.54, 29.05, -5.72, 9.77, -32.55, -0.68, 7.43, -76.73, -91.89, -8.99, 16.75, 80.73]
                mov_time = 1.5
	elif(command == 15): #jugada32
                motor_angles = [18.42, -17.37, 73.01, -2.15, 32.57, -5.43, 10.06, -34.04, -0.68, 16.04, -76.73, -86.09, 5.69, 23.52, 88.99]
                mov_time = 1.5
	elif(command == 16): #jugada33
                motor_angles = [27.12, -30.47, 76.79, -2.59, 33.45, -5.72, 9.77, -42.48, -0.59, 5.85, -76.9, -73.43, 11.76, 20.97, 91.54]
                mov_time = 1.5
	elif(command == 17):  #dab
		motor_angles = [8.57,0.74,50.15,-14.81,19.82,-80.79,8.01,-92.33,98.84,-105.19,67.36,-95.32,12.81,77.23,-3.58]
		mov_time = 1.5
	elif (command == 98): #saludo
		motor_angles = [5.41,-5.51,75.74,-26.95,12.35,-4.25,0.67,-0.2,10.31,-20.0,-76.55,-102.97,4.55,17.98,68.24]
		mov_time=1.5
	elif (command == 99):
		electromagnet_control(electromagnet,1)
		print "EM on"
	elif (command == 100):
		electromagnet_control(electromagnet,0)
		print "EM off"
	elif(command == 69):
		bucle=False

	elif(command == -1):
		my_string = str(poppy.motors)
		my_string = my_string.replace("<DxlMotor name=abs_z id=33 pos=",'')
		my_string = my_string.replace("<DxlMotor name=abs_x id=32 pos=",'')
		my_string = my_string.replace("<DxlMotor name=abs_y id=31 pos=",'')
		my_string = my_string.replace("<DxlMotor name=bust_y id=34 pos=",'')
		my_string = my_string.replace("<DxlMotor name=bust_x id=35 pos=",'')
		my_string = my_string.replace("<DxlMotor name=head_z id=36 pos=",'')
		my_string = my_string.replace("<DxlMotor name=head_y id=37 pos=",'')
		my_string = my_string.replace("<DxlMotor name=l_shoulder_y id=41 pos=",'')
		my_string = my_string.replace("<DxlMotor name=l_shoulder_x id=42 pos=",'')
		my_string = my_string.replace("<DxlMotor name=l_arm_z id=43 pos=",'')
		my_string = my_string.replace("<DxlMotor name=l_elbow_y id=44 pos=",'')
		my_string = my_string.replace("<DxlMotor name=r_shoulder_y id=51 pos=",'')
		my_string = my_string.replace("<DxlMotor name=r_shoulder_x id=52 pos=",'')
		my_string = my_string.replace("<DxlMotor name=r_arm_z id=53 pos=",'')
		my_string = my_string.replace("<DxlMotor name=r_elbow_y id=54 pos=",'')
		my_string = my_string.replace(">",'')
		print my_string 
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
	
