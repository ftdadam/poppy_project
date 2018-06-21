from random import randint
import numpy as np

w, h = 3, 3

def print_board(board):
	print "========="
	for ptr in range (w):
		print board[ptr]
	print "========="

def play(row,col,board,current_player,current_winner,n_play,player_1,player_2,empty):
	if(current_winner == empty):
		board [row][col] = current_player
		if(check_win(board,current_player)):
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
	elif(current_winner == 'None'):
		print "Tie, reset the game"
	else:
		print "Winner: " + str(current_player) + ", reset the game"
	return (board, current_winner, current_player)

def validate_move(row,col,board,empty):
	if(board [row][col] == empty):
		return True
	else:
		return False

def check_win(board,current_player):
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
	
def reset(player_1,player_2,empty,poppy_player_number):
	current_player = player_1
	current_winner = empty
	if(poppy_player_number == 1):
		robot = player_1
		first_move = True
	else:
		robot =  player_2
		first_move = False
	board = [[empty for x in range(w)] for y in range(h)]
	n_play = 0
	print "Start!"
	print_board(board)
	return robot, board, n_play, current_winner, current_player,first_move

# FUNCTIONS THAT CHECK WINNING CONDITIONS

def check_hor(board,empty,player_1,player_2):
	flag = False
	aux_X, aux_O = 3, 3
	empty_rows = []
	for i in range(3):
		if(board[i][0] == empty or board[i][1] == empty or board[i][2] == empty):
			empty_rows.append(i)
	for i in empty_rows:
		quant_X, quant_O = 0, 0
		for j in range(0,3):
			if board[i][j] == player_1:
				quant_X += 1
			elif board[i][j] == player_2:
				quant_O += 1
		if quant_X == 2:
			aux_X = i
			flag = True 
		if quant_O == 2:
			aux_O = i
			flag = True
	return flag, aux_X, aux_O

def check_ver(board,empty,player_1,player_2):
	flag = False
	aux_X, aux_O = 3, 3
	empty_cols = []
	for i in range(3):
		if(board[0][i] == empty or board[1][i] == empty or board[2][i] == empty):
			empty_cols.append(i)
	for j in empty_cols:
		quant_X, quant_O = 0, 0
		for i in range(0,3):
			if board[i][j] == player_1:
				quant_X += 1
			elif board[i][j] == player_2:
				quant_O += 1
			if quant_X == 2:
				aux_X = j
				flag = True 
			if quant_O == 2:
				aux_O = j
				flag = True
	return (flag, aux_X, aux_O)

def check_main_diag(board,empty,player_1,player_2):
	flag = False
	if (board[0][0] == empty or board[1][1] == empty or board[2][2] == empty):
		quant_X, quant_O = 0, 0
		for i in range(3):
			if board[i][i] == player_1:
				quant_X += 1
			if board[i][i] == player_2:
				quant_O += 1
		if quant_X == 2 or quant_O == 2:
			flag = True	
	return flag

def check_sec_diag(board,empty,player_1,player_2):
	flag = False
	if (board[0][2] == empty or board[1][1] == empty or board[2][0] == empty):
		quant_X, quant_O = 0, 0
		for i in range(3):
			if board[i][2-i] == player_1:
				quant_X += 1
			if board[i][2-i] == player_2:
				quant_O += 1
		if quant_X == 2 or quant_O == 2:
			flag = True	
	return flag


# FUNCTIONS THAT FIND EMPTY BOX IN A LINE OR A COLUMN

def find_hole_in_row(board,i,empty):
	for j in range(3):
		if board[i][j] == empty:
			return j

def find_hole_in_col(board,j,empty):
	for i in range(3):
		if board[i][j] == empty:
			return i


# FUNCTIONS THAT DEFINE THE MOVEMENT TO COMPLETE A LINE
def move_hor(board,robot,empty,player_1,player_2,aux_X, aux_O):
	if robot == player_1:
		if aux_X < 3:
			row = aux_X
			col = find_hole_in_row(board, row,empty)
		elif aux_O < 3:
			row = aux_O
			col = find_hole_in_row(board,row,empty)
	else:
		if aux_O < 3:
			row = aux_O
			col = find_hole_in_row(board,row,empty)
		elif aux_X < 3:
			row = aux_X
			col = find_hole_in_row(board,row,empty)
	return row, col	

def move_ver(board,robot,empty,player_1,player_2,aux_X, aux_O):
	if robot == player_1:
		if aux_X < 3:
			col = aux_X
			row = find_hole_in_col(board,col,empty)
		elif aux_O < 3:
			col = aux_O
			row = find_hole_in_col(board,col,empty)
	else:
		if aux_O < 3:
			col = aux_O
			row = find_hole_in_col(board,col,empty)
		elif aux_X < 3:
			col = aux_X
			row = find_hole_in_col(board,col,empty)
	return row, col

def move_md(board,empty):
	for i in range(3):
		if board[i][i] == empty:
			row, col = i, i
			return row, col	

def move_sd(board,empty):
	for i in range(3):
		if board[i][2-i] == empty:
			row, col = i, 2-i
			return row, col	

# FUNCTION THAT MAKES THE MOVEMENT

def make_move(board,robot,empty,player_1,player_2):
	flag_h, aux_X_h, aux_O_h = check_hor(board,empty,player_1,player_2)
	flag_v, aux_X_v, aux_O_v = check_ver(board,empty,player_1,player_2)
	test_md = check_main_diag(board,empty,player_1,player_2)
	test_sd = check_sec_diag(board,empty,player_1,player_2)
	if flag_h:
		row, col = move_hor(board,robot,empty,player_1,player_2,aux_X_h, aux_O_h)
	elif flag_v:
		row, col = move_ver(board,robot,empty,player_1,player_2,aux_X_v, aux_O_v)
	elif test_md:
		row, col = move_md(board,empty)
	elif test_sd:
		row, col = move_sd(board,empty)
	else:
		row = randint(0,2)
		col = randint(0,2)
	return row, col