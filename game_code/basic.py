import time
from random import randint
from grovepi import *

# Connect the Grove Electromagnet to digital port D4
electromagnet = 4
pinMode(electromagnet,"OUTPUT")
time.sleep(1)
poppy = PoppyTorso()


w, h = 3, 3
empty = ' '
player_1 = 'X'
player_2 = 'O'
robot = player_2
board = [[empty for x in range(w)] for y in range(h)]
n_play = 0
current_player = player_1
current_winner = empty


def print_board(board):
	print "========="
	for ptr in range (w):
		print board[ptr]
	print "========="

def play(row,col,board,current_player,current_winner, n_play):
	if(current_winner == empty):
		n_play = n_play+1
		board [row][col] = current_player
		if(check_win()):
			print "Winner: " + str(current_player) + ", reset the game"
			current_winner = current_player
		else:
			if(n_play < 9):
				if(current_player == player_1):
					current_player = player_2
				else:
					current_player = player_1
			else:
				print "Tie, reset the game"
				current_winner = 'None'
	else:
		print "Winner: " + str(current_player) + ", reset the game"
	return (board, n_play, current_winner, current_player)

def validate_move(row,col,board):
	global empty
	if(board [row][col] == empty):
		return True
	else:
		return False

def check_win():
	global current_player
	isWin = False
	for row in range(h):
		if(board[row][0] == current_player and board[row][1] == current_player and board[row][2] == current_player):
			isWin = True
	for col in range(w):
		if(board[0][col] == current_player and board[1][col] == current_player and board[2][col] == current_player):
			isWin = True
	if(board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player):
		isWin = True
	if(board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player):
		isWin = True
	return isWin

def set_poppy_player(player_1, player_2):
	value = int(raw_input("Player Number for Poppy (1 or 2): << "))
	while(value != 1 and value != 2):
		value = int(raw_input("Incorrect number, try again (1 or 2): << "))
	if(value == 1):
		return player_1
	else:
		return player_2

def reset():
	global poppy
	current_player = player_1
	current_winner = empty
	robot = set_poppy_player(player_1, player_2)
	board = [[empty for x in range(w)] for y in range(h)]
	n_play = 0
	poppy.init_position.start()
	print "Start!"
	print_board(board)
	return robot, board, n_play, current_winner, current_player

(robot, board, n_play, current_winner, current_player) = reset()

def poppy_movement(row,col,n_play):
	global poppy

	(x,y,z) = (0.0,0.0,0.0)

	# get the piece
	x = 0.4
	y = 0.4
	if(n_play <= 2):
		z = -0.6
	elif(n_play <= 4):
		z = -0.5
	elif(n_play <= 6):
		z = -0.4
	elif(n_play <= 8):
		z = -0.3
	else:
		z = -0.2

	poppy.r_arm_chain.goto((x,y,z), 1., wait=True)

	# turn on electromagnet
	electromagnet_control(1)

	# move the hand
	z = -0.2
	if(row == 0):
		x = 0.6
	elif(row == 1):
		x = 0.8
	else:
		x = 1.0

	if(col == 0):
		y = 0.6
	elif(col == 1):
		y = 0.8
	else:
		y = 1.0

	poppy.r_arm_chain.goto((x,y,z), 1., wait=True)

	# turn off electromagnet

	electromagnet_control(0)

	# restart position

	poppy.init_position.start()

def electromagnet_control(state):
	try:
        digitalWrite(led,state)		# Send 1 to switch on the electromagnet, 0 to swtch it off
        time.sleep(1)
    except KeyboardInterrupt:
        digitalWrite(led,0)
    except IOError:
        print ("Error")

while(1):
	while(current_winner == empty):
		if(current_player == robot):
			print("Poppy's Turn...")
			isValid = False
			while(not(isValid)):
				row = randint(0,2)
				col = randint(0,2)
				isValid = validate_move(row,col,board)
			(board, n_play, current_winner, current_player) = play(row,col,board,current_player,current_winner, n_play)
			print ("Poppy's moving his hand...")
			time.sleep(0.5)
		else:
			print("Your Turn...")
			isValid = False
			while(not(isValid)):
				row = int(raw_input("Row: << "))
				col = int(raw_input("Col: << "))
				if (row > 2 or row < 0 or col > 2 or col < 0):
					print "Out of range, re-enter values"
				else:
					isValid = validate_move(row,col,board)
					if(not(isValid)):
						print  "Already taken! Try again"
			(board, n_play, current_winner, current_player) = play(row,col,board,current_player,current_winner, n_play)
		print_board(board)
	(robot, board, n_play, current_winner, current_player) = reset()