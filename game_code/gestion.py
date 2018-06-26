import time
from random import randint
from pypot.robot import from_json
from grovepi import *
from strategy import *
from movements import *


# === create a robot object from json config file === 
poppy=from_json("/home/poppy/miniconda/lib/python2.7/site-packages/poppy_torso/configuration/poppy_torso_new.json")
for m in poppy.motors:
	m.compliant=False
time.sleep(1)

# === global constants ===

w, h = 3, 3
empty = ' '
player_1 = 'X'
player_2 = 'O'
robot = player_2
board = [[empty for x in range(w)] for y in range(h)]
n_play = -1
current_player = player_1
current_winner = empty

polling = True
first_move = True
robot_move = False
human_move = False
reset_move = False

# === main loop ===

while(1):

	# === file polling loop ===
	while(polling):
		file_data = []
		file  = open('data', 'r')
		for line in file:
			file_data.append(int(line))
		n_play_file, row, col = file_data[0], file_data[1], file_data[2]
		time.sleep(0.5)

		if((n_play_file == -1 and n_play != 0 and robot != player_1) or (current_winner != empty and n_play_file == -1)):
			n_play = n_play_file
			file.close()
			reset_move = True
			poppy_player_number = file_data[1]
			polling = False
		elif((robot == player_2 and n_play_file%2 != 0) or (robot == player_1 and n_play_file%2 == 0)):
			if (n_play_file > n_play):
				n_play = n_play_file
				file.close()
				human_move = True
				polling = False
		elif(robot == player_1 and n_play == 0 and first_move):
			robot_move = True
			polling = False

	if(human_move):
		(board, current_winner, current_player) = play(row,col,board,current_player,current_winner, n_play,player_1,player_2,empty)
		robot_action(current_winner, poppy,robot,empty)
		print_board(board)
		human_move = False
		if(current_winner == empty):
			robot_move = True
		else:
			polling = True
	if(robot_move):
		isValid = False
		n_play = n_play + 1
		while(not(isValid)):
			(row, col) = make_move(board,robot,empty,player_1,player_2)
			isValid = validate_move(row,col,board,empty)
		(board, current_winner, current_player) = play(row,col,board,current_player,current_winner,n_play,player_1,player_2,empty)
		
		robot_play(n_play,robot,player_1,player_2,row,col,poppy)
		robot_action(current_winner, poppy,robot,empty)

		print_board(board)
		robot_move = False
		if(robot == player_1 and first_move):
			first_move = False
		polling = True
	if(reset_move):
		(robot, board, n_play, current_winner, current_player,first_move) = reset(player_1,player_2,empty,poppy_player_number)
		initial_pos(poppy)
		wave(poppy)
		initial_pos(poppy)
		reset_move = False
		polling = True
