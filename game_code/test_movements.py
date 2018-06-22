
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
motor_angles = [0,0,45,0,5,-5,0,-10,15,20,-10,-180,0,-20,0]
mov_time=1.5
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
		motor_angles = [-33.89, -7.97, 36.79, 22.73, 1.8, -5.13, 12.7, -18.57, 34.84, 57.54, -67.14, -136.46, -5.91, -15.34, 60.68]
		mov_time = 1.5
	elif (command == 3): #pieza2
		motor_angles = [-39.16, -6.3, 44.53, 18.95, 10.15, -5.43, 12.7, -28.77, 29.91, 63.34, -67.76, -133.91, -6.53, -9.36, 58.92]
		mov_time = 1.5
	elif(command == 4): #pieza3
		motor_angles = [-37.14, -5.95, 43.56, 22.02, 9.27, -5.43, 12.7, -32.2, 29.47, 61.32, -67.93, -135.93, -8.02, -10.24, 53.82]
		mov_time = 1.5
	elif(command == 5): #pieza4
		motor_angles = [-34.51, -5.07, 43.74, 24.04, 10.59, -5.43, 12.7, -36.33, 27.71, 59.47, -68.11, -135.76, -8.29, -13.49, 51.1]
		mov_time = 1.5
	elif(command == 6): #pieza5
		motor_angles = [-30.46, -5.15, 45.14, 24.22, 15.08, -5.13, 12.7, -38.53, 23.85, 58.15, -68.37, -136.9, -10.4, -17.8, 46.44]
		mov_time = 1.5
	elif(command == 7):  #jugada11
		motor_angles = [-6.99, -3.22, 41.01, 12.88, 11.74, -6.6, 11.82, -31.32, 35.63, 28.97, -59.14, -141.12, -6.97, -1.45, 54.26]
		mov_time = 1.5
	elif(command == 8): #jugada12
		motor_angles = [2.86, -8.67, 39.6, 11.38, 16.92, -6.6, 11.82, -31.58, 29.03, 17.98, -59.23, -148.07, 5.6, 22.99, 48.9]
		mov_time=1.5
	elif(command == 9): #jugada13
		motor_angles = [26.95, -19.04, 46.55, 5.93, 30.99, -6.6, 11.82, -36.33, 13.47, 5.41, -58.88, -132.51, 9.74, 36.62, 55.41]
		mov_time = 1.5
	elif(command == 10): #jugada21
		motor_angles = [-6.81, 1.7, 69.23, -8.04, 14.2, -6.89, 11.82, -13.12, 15.14, 39.52, -69.08, -118.79, -6.62, 8.31, 65.87]
		mov_time = 1.5
	elif(command == 11): #jugada22
                motor_angles = [1.19, -7.44, 68.09, -11.82, 17.1, -6.6, 11.82, -14.97, 11.36, 24.4, -69.87, -128.99, 6.57, 17.54, 63.41]
                mov_time = 1.5
	elif(command == 12): #jugada23
                motor_angles = [21.85, -24.14, 67.03, -26.42, 25.98, -7.48, 11.82, -12.95, 14.44, 10.07, -76.9, -128.2, 3.23, 17.27, 69.21]
                mov_time = 1.5
	elif(command == 13): #jugada31
                motor_angles = [11.38, -4.98, 87.69, -26.51, 19.56, -6.6, 11.82, -21.65, 0.02, 20.53, -76.9, -88.37, -25.52, 11.3, 89.43]
                mov_time = 1.5
	elif(command == 14): #jugada32
                motor_angles = [11.47, -11.48, 87.16, -26.59, 21.49, -6.6, 11.82, -20.95, 0.55, 23.87, -76.9, -98.04, -5.74, 18.86, 84.86]
                mov_time = 1.5
	elif(command == 15): #jugada33
                motor_angles = [17.36, -29.59, 94.11, -27.21, 14.29, -6.6, 11.82, -32.99, 5.82, 3.47, -76.9, -86.0, 1.38, 7.78, 88.81]
                mov_time = 1.5
	elif(command == 16):  #dab
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
	
