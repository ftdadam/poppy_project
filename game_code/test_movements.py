# Script 
# This script takes the robot to an rest position until waits for another order 
# Author: ABT, Juan Francisco. DADAM, Federico
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

# set grovepi+ port 4 as output
electromagnet = 4
pinMode(electromagnet,"OUTPUT")
time.sleep(1)

# create the robot object


# All motors are  compliant mode

command = int(raw_input("Position << "))
if (command == 0):
	motor_angles = [0,0,45,0,5,-5,0,10,15,20,-10,-180,0,-20,0]
	mov_time = 2
elif (command == 1):
	motor_angles = [-25.63,-2.43,44.97,9.63,5.41,-4.25,16.8,-13.82,18.4,51.21,-76.46,-127.14,3.67,-0.31,68.42]
	mov_time = 2
elif (command = 99)
	electromagnet_control(electromagnet,1)
elif (command = 100)
	electromagnet_control(electromagnet,0)

for ptr in range(0,15):
	poppy.motors[ptr].goto_position(motor_angles[ptr],mov_time)
	time.sleep(0.2)
time.sleep(3)



