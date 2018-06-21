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

def initial_pos(poppy):
	motor_angles = [0,0,45,0,5,-5,0,-10,15,20,-10,-180,0,-20,0]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	em_control(0)

def wave(poppy):
	em_control(0)
	mov_time = 2
	for i in range 3:
		motor_angles = [0.75, 5.13, 42.77, 3.56, 0.22, -5.43, 0.09, -35.71, 39.58, 46.81, -68.02, -170.92, 2.0, -12.88, 15.76]
		move_robot(poppy,motor_angles,mov_time)
		motor_angles = [-0.75, 4.69, 42.77, 3.74, -0.22, -5.43, 0.09, -37.12, 49.78, 49.36, -32.68, -171.1, 2.35, -12.97, 13.47]
		move_robot(poppy,motor_angles,mov_time)

def take_piece_1(poppy):
	# prepare to take a piece
	motor_angles = [-25.89, -3.66, 45.32, 10.15, 4.09, -5.13, 16.22, -14.18, 17.87, 51.38, -76.11, -169.96, 4.81, 4.26, -54.84]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# low the hand to the piece
	motor_angles = [-49.27, -0.76, 48.57, 9.98, -1.19, -3.08, 15.92, -15.14, 37.38, 27.74, -76.9, -146.31, 6.66, -9.27, 46.62]
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
	motor_angles = [-45.32, 1.88, 53.58, 11.56, 1.71, -3.08, 15.92, -22.7, 34.48, 26.77, -76.9, -148.59, 5.78, -14.11, 34.4]
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
	motor_angles = [-43.82, 2.23, 54.81, 12.26, 1.8, -3.08, 15.92, -24.55, 34.48, 25.19, -76.81, -147.27, 4.73, -14.46, 36.24]
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
	motor_angles = [-39.08, 2.93, 54.73, 10.33, 6.73, -30.06, 15.34, -36.77, 24.37, 25.1, -76.9, -153.08, 2.88, -20.53, 30.09]
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
	motor_angles = [-37.05, 2.14, 54.81, 11.74, 7.52, -30.06, 15.34, -37.91, 23.85, 23.87, -76.81, -151.76, 0.33, -20.62, 33.34]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)

def move_to_board(poppy,row,col):
	# move to the center of the board
	mov_time = 1.5
	motor_angles = [23.08,-4.1,50.68,-2.86,16.57,-9.53,10.06,-4.95,11.01,-25.63,-76.81,-133.91,-1.34,17.98,45.16]
	move_robot(poppy,motor_angles,mov_time)
	
	# select where to play

	if(row == 0):
		if(col == 0):
			motor_angles = [22.73, -38.21, 84.18, -27.38, 24.04, -3.96, 4.78, -45.74, 25.34, -20.53, -74.0, -87.05, -10.84, 2.15, 91.63]
		elif(col == 1):
			motor_angles = [11.56, -7.88, 88.84, -16.92, 7.78, -3.96, 4.78, -29.21, 23.85, -17.36, -73.65, -98.31, -1.34, 4.88, 72.37]
		elif(col == 2):
			motor_angles = [8.92, 10.49, 94.02, -22.99, 0.04, -3.96, 4.78, -28.07, 17.69, -17.8, -74.09, -93.47, -10.66, 2.95, 78.88]
	elif(row == 1):
		if(col == 0):
			motor_angles = [25.63, -17.73, 64.92, -0.31, 12.79, -3.96, 5.07, -25.87, 27.63, -18.42, -73.3, -112.11, 9.3, 16.31, 64.55]
		elif(col == 1):
			motor_angles = [-1.27, -2.25, 70.29, -6.11, 12.44, -3.96, 4.78, -20.86, 15.67, 16.4, -72.68, -121.52, 10.97, 22.46, 65.08]
		elif(col == 2):
			motor_angles = [-12.0, 11.29, 76.44, -17.63, 5.76, -3.96, 4.78, -16.37, 15.41, 38.55, -73.91, -122.22, 1.74, 10.59, 64.73]
	elif(row == 2):
		if(col == 0):
			motor_angles = [16.31, -24.05, 58.68, -12.26, 23.96, -3.96, 4.49, -12.77, 16.55, 39.25, -72.51, -149.3, 10.79, 36.7, 43.27]
		elif(col == 1):
			motor_angles = [4.53, -6.03, 37.32, 28.09, 14.37, -3.96, 4.78, -19.63, 16.55, 43.03, -73.03, -135.14, 6.92, 20.88, 44.07]
		elif(col == 2):
			motor_angles = [-19.91, 3.73, 49.8, 16.66, 11.82, -3.96, 4.78, -18.92, 4.33, 59.38, -73.3, -128.9, -1.16, 11.74, 50.31]

	move_robot(poppy,motor_angles,mov_time)
	em_control(0)
	initial_pos(poppy)


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

	move_to_board(poppy,row,col)
	initial_pos

def robot_action(current_winner, poppy,robot,empty):
	mov_time=1.5
	if (current_winner==empty):
		return 
	elif(current_winner==robot):
		motor_angles = [8.57,0.74,50.15,-14.81,19.82,-80.79,8.01,-92.33,98.84,-105.19,67.36,-95.32,12.81,77.23,-3.58]
	else:
		motor_angles = [5.41,-5.51,75.74,-26.95,12.35,-4.25,0.67,-0.2,10.31,-20.0,-76.55,-102.97,4.55,17.98,68.24]
	move_robot(poppy,motor_angles,mov_time)
	em_control(0)

