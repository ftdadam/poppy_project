# FUNCTIONS THAT CHECK IF THERE ARE WINNING CONDITIONS
def check_hor(board):
	flag = False
	aux_X, aux_O = 3, 3
	for i in range(3):
		quant_X, quant_O = 0, 0
		for j in range(0,3):
			if board[i][j] == 'X':
				quant_X += 1
			elif board[i][j] == 'O':
				quant_O += 1
		if quant_X == 2:
			aux_X = i
			flag = True 
		if quant_O == 2:
			aux_O = i
			flag = True
	return [flag, aux_X, aux_O]

def check_ver(board):
	flag = False
	aux_X, aux_O = 3, 3
	for j in range(3):
		quant_X, quant_O = 0, 0
		for i in range(0,3):
			if board[i][j] == 'X':
				quant_X += 1
			elif board[i][j] == 'O':
				quant_O += 1
		if quant_X == 2:
			aux_X = j
			flag = True
		elif quant_O == 2:
			aux_O = j
			flag = True
	return [flag, aux_X, aux_O]

def check_main_diag(board):
	flag = False
	for i in range(3):
		if board[i][i] == 'X'
			quant_X += 1
		if board[i][i] = 'O'
			quant_O += 1
	if quant_X == 2 or quant_O == 2:
		flag = True	
	return flag

def check_sec_diag(board):
	flag = False
	for i in range(3):
		if board[i][2-i] == 'X'
			quant_X += 1
		if board[i][2-i] = 'O'
			quant_O += 1
	if quant_X == 2 or quant_O == 2:
		flag = True	
	return flag	


# FUNCTIONS THAT FIND THE EMPTY BOX
def find_hole_in_line(board,i):
	for j in range(3):
		if board[i][j] == empty:
			return j
def find_hole_in_col(board,j):
	for i in range(3):
		if board[i][j] == empty:
			return i


# FUNCTIONS THAT DEFINES THE MOVEMENT TO COMPLETE A LINE
def move_hor(board):
	test = check_hor(board)
	if test[0] == True:
		if poppy == player_1:
			if test[1] < 3:
				row = test[1]
				col = find_hole_in_line(board, row)
				return row, col
			elif test[2] < 3:
				row = test[2]
				col = find_hole_in_line(board,row)
				return row, col			

		elif poppy == player_2:
			if test[2] < 3:
				row = test[2]
				col = find_hole_in_line(board,row)
				return row, col
		
			elif test[1] < 3:
				row = test[1]
				col = find_hole_in_line(board,row)
				return row, col

def move_ver(board):
	test = check_ver(board)
	if test[0] == True:
		if poppy == 1:
			if test[1] < 3:
				col = test[1]
				row = find_hole_in_col(board,col)
				return row, col
			elif test[2] < 3:
				col = test[2]
				row = find_hole_in_col(board,col)
				return row, col

		elif poppy == 2:
			if test[2] < 3:
				col = test[2]
				row = find_hole_in_col(board,col)
				return row, col
			if test[1] < 3:
				col = test[1]
				row = find_hole_in_col(board,col)
				return row, col

def move_md(board):
	for i in range(3):
		if board[i][i] == empty:
			row, col = i, i
			return row, col	

def mode_sd(board):
	for i in range(3):
		if board[i][2-i] == empty:
			row, col = i, 2-i
			return row, col	


# FUNCTION THAT MAKES THE MOVEMENT
def make_move(board):
	test_h = check_hor(board)
	test_v = check_ver(board)
	test_md = check_main_diag(board)
	test_sd = check_sec_diag(board)
	if test_h[0]:
		row, col = move_h(board)
	elif test_v[0]:
		row, col = move_v
	elif test_md[0]:
		row, col = move_md(board)
	elif test_sd[0]:
		row, col = move_sd(board)
	else:
		row = randint(0,2)
		col = randint(0,2)
	return row, col
