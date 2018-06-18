import time
from random import randint
# from grovepi import *

# Connect the Grove Electromagnet to digital port D4
electromagnet = 4
# pinMode(electromagnet,"OUTPUT")
time.sleep(1)
# poppy = PoppyTorso()
w, h = 3, 3
empty = ' '
player_1 = 'X'
player_2 = 'O'
robot = player_2
board = [[empty for x in range(w)] for y in range(h)]
n_play = -1
current_player = player_1
current_winner = empty

from strategy import *

# poppy.init_position.start()

# def electromagnet_control(state):
# 	try:
#         digitalWrite(led,state)		# Send 1 to switch on the electromagnet, 0 to swtch it off
#         time.sleep(1)
#     except KeyboardInterrupt:
#         digitalWrite(led,0)
#     except IOError:
#         print ("Error")

polling = True
first_move = True
robot_move = False
human_move = False
reset_move = False


while(1):
	while(polling):
		file_data = []
		file  = open('data', 'r')
		for line in file:
			file_data.append(int(line))
		n_play_file, row, col = file_data[0], file_data[1], file_data[2]
		time.sleep(0.5)
		if(n_play_file == -2):
			print "putin"
		if((n_play_file == -1 and n_play != 0 and robot != player_1) or (current_winner != empty and n_play_file == -1)):
			print 'aca1'
			n_play = n_play_file
			file.close()
			reset_move = True
			polling = False
		elif((robot == player_2 and n_play_file%2 != 0) or (robot == player_1 and n_play_file%2 == 0)):
			if (n_play_file > n_play):
				print 'aca2'
				n_play = n_play_file
				file.close()
				human_move = True
				polling = False
		elif(robot == player_1 and n_play == 0 and first_move):
			print 'aca3'
			robot_move = True
			polling = False
	if(human_move):
		(board, current_winner, current_player) = play(row,col,board,current_player,current_winner, n_play,player_1,player_2,empty)
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
		print_board(board)
		robot_move = False
		if(robot == player_1 and first_move):
			first_move = False
		polling = True
	if(reset_move):
		(robot, board, n_play, current_winner, current_player,first_move) = reset(player_1,player_2,empty)
		reset_move = False
		polling = True
		