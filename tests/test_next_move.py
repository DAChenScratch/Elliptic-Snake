from app.next_move import next_move
import numpy as np
def test_next_move():
	x = np.array([[0,0,0,0],[1,1,0,0],[0,0,0,0],[0,1,1,0]])
	head = [2,3]
	target = [0,0]
	next_move(x,head,target)