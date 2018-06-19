import time
from grovepi import *

# === set grovepi+ port 4 as output ===

em = 4
pinMode(em,"OUTPUT")
def em_control(state):
	em = 4
	try:
		digitalWrite(em,state)	# 1: Switch on, 0: Switch off
		time.sleep(1)
	except KeyboardInterrupt:
		digitalWrite(em,0)
	except IOError:
		digitalWrite(em,0)
		print ("Error")

def move_robot(poppy,motor_angles,mov_time):
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

def initial_pos():
	motor_angles = [0,0,45,0,5,-5,0,-10,15,20,-10,-180,0,-20,0]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	
def take_piece_1(poppy):
	# prepare to take a piece
	motor_angles = [-25.89, -3.66, 45.32, 10.15, 4.09, -5.13, 16.22, -14.18, 17.87, 51.38, -76.11, -169.96, 4.81, 4.26, -54.84]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# low the hand to the piece
	motor_angles = [-25.71, -4.63, 45.23, 10.51, 3.47, -6.6, 12.7, -14.09, 17.6, 51.65, -49.91, -160.46, 9.65, -4.18, 30.18]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)

def take_piece_2(poppy):
	# prepare to take a piece
	motor_angles = [-25.89, -3.66, 45.32, 10.15, 4.09, -5.13, 16.22, -14.18, 17.87, 51.38, -76.11, -169.96, 4.81, 4.26, -54.84]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# low the hand to the piece
	motor_angles = [-32.57, 0.65, 39.69, 20.26, -5.32, -4.25, 15.92, -15.14, 21.65, 49.1, -76.9, -150.79, 12.2, 6.11, 35.45]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)

def take_piece_3(poppy):
	# prepare to take a piece
	motor_angles = [-25.89, -3.66, 45.32, 10.15, 4.09, -5.13, 16.22, -14.18, 17.87, 51.38, -76.11, -169.96, 4.81, 4.26, -54.84]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# low the hand to the piece
	motor_angles = [-25.98, 0.12, 33.1, 18.07, 0.13, -4.25, 15.34, -12.95, 17.96, 49.36, -76.73, -154.84, 2.7, 8.31, 38.97]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)

def take_piece_4(poppy):
	# prepare to take a piece
	motor_angles = [-25.89, -3.66, 45.32, 10.15, 4.09, -5.13, 16.22, -14.18, 17.87, 51.38, -76.11, -169.96, 4.81, 4.26, -54.84]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# low the hand to the piece
	motor_angles = [-11.47, 6.01, 37.93, 13.76, -7.43, -4.25, 15.92, -21.47, 25.16, 33.63, -69.6, -169.6, 4.73, -2.24, 29.56]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)

def take_piece_5(poppy):
	# prepare to take a piece
	motor_angles = [-25.89, -3.66, 45.32, 10.15, 4.09, -5.13, 16.22, -14.18, 17.87, 51.38, -76.11, -169.96, 4.81, 4.26, -54.84]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# low the hand to the piece
	motor_angles = [-18.59, 1.09, 36.97, 16.92, 3.21, -4.25, 15.92, -9.08, 12.15, 27.47, -74.79, -159.58, -4.15, 10.59, 37.21]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)

def move_to_board(row,col):
	# move to the center of the board
	mov_time = 1.5
	motor_angles = [23.08,-4.1,50.68,-2.86,16.57,-9.53,10.06,-4.95,11.01,-25.63,-76.81,-133.91,-1.34,17.98,45.16]
	move_robot(poppy,motor_angles,mov_time)
	
	# select where to play

	if(row == 0):
		if(col == 0):
			motor_angles = [23.16, -4.89, 50.95, -3.03, 15.34, -5.43, 10.35, -5.21, 11.36, -25.54, -76.46, -189.12, -5.47, -4.44, 6.09]
		elif(col == 1):
			motor_angles = [22.81, -4.8, 50.86, -3.12, 15.69, -5.43, 10.06, -5.21, 11.36, -25.54, -76.46, -165.38, -10.92, 41.8, 21.91]
		elif(col == 2):
			motor_angles = [35.82, -11.57, 47.78, -5.32, 16.75, -5.43, 10.06, -11.45, 9.43, -12.7, -74.53, -150.09, 9.56, 32.04, 51.19]
	elif(row == 1):
		if(col == 0):
			motor_angles = [7.43, -11.13, 48.31, -2.07, 25.54, -5.43, 10.06, -6.18, 1.87, -5.58, -74.88, -138.13, -8.02, 10.51, 60.15]
		elif(col == 1):
			motor_angles = [16.66, -11.04, 48.4, -5.23, 25.01, -5.43, 10.06, -5.47, 2.48, 0.04, -74.79, -137.16, 1.21, 20.35, 64.64]
		elif(col == 2):
			motor_angles = [32.22, -20.8, 56.4, -8.13, 25.54, -5.43, 10.06, -15.49, 4.07, -12.35, -74.88, -125.38, 5.08, 24.31, 64.2]
	elif(row == 2):
		if(col == 0):
			motor_angles = [13.58, -13.07, 70.99, -1.54, 29.05, -5.72, 9.77, -32.55, -0.68, 7.43, -76.73, -91.89, -8.99, 16.75, 80.73]
		elif(col == 1):
			motor_angles = [18.42, -17.37, 73.01, -2.15, 32.57, -5.43, 10.06, -34.04, -0.68, 16.04, -76.73, -86.09, 5.69, 23.52, 88.99]
		elif(col == 2):
			motor_angles = [27.12, -30.47, 76.79, -2.59, 33.45, -5.72, 9.77, -42.48, -0.59, 5.85, -76.9, -73.43, 11.76, 20.97, 91.54]

	move_robot(poppy,motor_angles,mov_time)
	em_control(0)


def robot_play(n_play,robot,player_1,player_2,row,col,poppy):
	if((robot == player_1 and n_play == 1) or (robot == player_2 and n_play == 2)):
		take_piece_1(poppy)
	elif((robot == player_1 and n_play == 3) or (robot == player_2 and n_play == 4)):
		take_piece_2(poppy)
	elif((robot == player_1 and n_play == 5) or (robot == player_2 and n_play == 6)):
		take_piece_3(poppy)
	elif((robot == player_1 and n_play == 7) or (robot == player_2 and n_play == 8)):
		take_piece_4(poppy)
	elif(robot == player_1 and n_play == 9):
		take_piece_5(poppy)

	move_to_board(row,col)
	initial_pos
