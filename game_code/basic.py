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
n_play = 0
current_player = player_1
current_winner = empty

from prueba_estrategia import *

(robot, board, n_play, current_winner, current_player) = reset(player_1,player_2,empty)

# poppy.init_position.start()

# def electromagnet_control(state):
# 	try:
#         digitalWrite(led,state)		# Send 1 to switch on the electromagnet, 0 to swtch it off
#         time.sleep(1)
#     except KeyboardInterrupt:
#         digitalWrite(led,0)
#     except IOError:
#         print ("Error")

while(1):
	while(current_winner == empty):
		if(current_player == robot):
			print("Poppy's Turn...")
			isValid = False
			while(not(isValid)):
				# row = randint(0,2)
				# col = randint(0,2)
				(row, col) = make_move(board,robot,empty,player_1,player_2)
				isValid = validate_move(row,col,board,empty)
			(board, n_play, current_winner, current_player) = play(row,col,board,current_player,current_winner, n_play,player_1,player_2,empty)
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
					isValid = validate_move(row,col,board,empty)
					if(not(isValid)):
						print  "Already taken! Try again"
			(board, n_play, current_winner, current_player) = play(row,col,board,current_player,current_winner, n_play,player_1,player_2,empty)
		print_board(board)
	(robot, board, n_play, current_winner, current_player) = reset(player_1,player_2,empty)