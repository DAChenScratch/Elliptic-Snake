import numpy as np

def find_safe_move(x,y, board, snakes):
	#board states given in system [z,y,x] 
	directions = ['up', 'down', 'left', 'right']
	
	#3 is the check right
	#2 is the check left
	#1 is the check down
	#0 is the check up
	for i in range(3,-1,-1):
		safe = False
		if(i == 3):
			#stay in the game board!
			if(x+1 >= board.shape[1]):
				del directions[i]
				continue
				
			#check if otherwise safe
			safe = check_square(x+1,y,board)
			
		if(i == 2):
			#stay in the game board!
			if(x-1 < 0):
				del directions[i]
				continue
				
			#check if otherwise safe
			safe = check_square(x-1,y,board)
			
		if(i == 1):
			#stay in the game board!
			if(y+1 >= board.shape[0]):
				del directions[i]
				continue
				
			#check if otherwise safe
			safe = check_square(x,y+1,board)
		if(i == 0):
		
			#stay in the game board
			if(y-1 < 0):
				del directions[i]
				continue
				
			#check if otherwise safe
			safe = check_square(x,y-1,board)
			
		if not safe:
			del directions[i]

	return directions
	
	
#checks the given square for safety. 			
def check_square(x,y,board):
	#check if empty or food
	if(board[0,y,x] == (0 or 4)):
		return True
		
	#check if body or tail (will still be unsafe after next move.
	if(board[0,y,x] == (2 or 1)):
		return False
		
	#if it is a tail it might become safe next turn. check!
	if(board[0,y,x] == 3):
		#check if that tails head is by food or if it is your own tail.(safe in both cases) 
		x=1
	return True
	
	
	
	
