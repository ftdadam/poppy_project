import numpy as np

file_name = 'data'
file = open(file_name)
data_raw = []
data_raw = [x for x in file.readlines()]

w, h = 3, 3
empty = ' '
player_1 = 'X'
player_2 = 'O'
board = [[empty for x in range(w)] for y in range(h)]
ids = []
x_pos = []
y_pos = []

# for ptr in range(0,len(data_raw)):
# 	print data_raw[ptr]

for ptr in range (0,len(data_raw)):
	data = data_raw[ptr].split()
	ids.append(float(data[2]))
	x_pos.append(float(data[4]))
	y_pos.append(float(data[5]))

file.close()



def isPlayer(id,player_1,player_2):
	if(id < 5):
		return player_1
	else:
		return player_2

x_lim = [0.0,10.0,20.0,30.0]
y_lim = [0.0,10.0,20.0,30.0]

for ptr in range(0,len(ids)):
	player = isPlayer(ids[ptr],player_1,player_2)
	
	x_pointer = -1
	y_pointer = -1

	if(x_pos[ptr] >= x_lim[0] and x_pos[ptr] <= x_lim[1]):
		x_pointer = 0
	elif(x_pos[ptr] > x_lim[1] and x_pos[ptr] <= x_lim[2]):
		x_pointer = 1
	elif(x_pos[ptr] > x_lim[2] and x_pos[ptr] <= x_lim[3]):
		x_pointer = 2

	if(y_pos[ptr] >= y_lim[0] and y_pos[ptr] <= y_lim[1]):
		y_pointer = 0
	elif(y_pos[ptr] > y_lim[1] and y_pos[ptr] <= y_lim[2]):
		y_pointer = 1
	elif(y_pos[ptr] > y_lim[2] and y_pos[ptr] <= y_lim[3]):
		y_pointer = 2

	# print x_pointer, y_pointer

	if(x_pointer == -1 or y_pointer == -1):
		print 'mal'
	else:
		print 'bien'
		board[x_pointer][y_pointer] = player

for ptr in range(0,h):
	print board[ptr]
