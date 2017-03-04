import numpy as np
import networkx as nx
import matplotlib.pyplot as plotter

#returns first move and the length
def next_move(board, head, target):
	G = nx.Graph()
	height, width = board.shape
	for i in range(height*width):
		G.add_node(i)

	for i in range(height*width):
		#1 is try right
		#2 is try left
		#3 is try up
		#4 is try down
		for j in range(1,5):
			if j == 1:
				#stay on the board
				if(i+1)%width == 0:
					continue
				elif ((board[lin_y(i,width),lin_x(i+1,width)] == 0)and (board[lin_y(i,width),lin_x(i,width)] == 0)):
					G.add_edge(i,i+1)
			if j == 2:
				if i%width == 0:
					continue	
				elif (board[lin_y(i,width),lin_x(i-1,width)] == 0)and (board[lin_y(i,width),lin_x(i,width)] == 0):
					G.add_edge(i,i-1)
			if j == 3:
				if i< width:
					continue
				elif (board[lin_y((i-width),width),lin_x(i,width)] == 0) and (board[lin_y(i,width),lin_x(i,width)] == 0):
					G.add_edge(i,i-width)
			if j == 4:
				if i+width >= (height*width):
					continue
				elif (board[lin_y((i+width),width),lin_x(i,width)] == 0) and (board[lin_y(i,width),lin_x(i,width)] == 0):
					G.add_edge(i,i+width)
	#done making graph G. now find a path and hope this works...
	
	
	path = nx.shortest_path(G,source=(head[1]*width+head[0]),target=(target[1]*width+target[0]))
	print(path)
	
def lin_x(x,width):
	x= x%width
	return x
def lin_y(y,width):
	y = y//width
	return y
if __name__ == "__main__":
	x = np.array([[0,0,0,0],[1,1,0,0],[0,0,0,0],[0,1,1,0]])
	head = [2,3]
	target = [0,0]
	next_move(x,head,target)
	
	y = np.array([
		[1,1,1,1,0,0,0,0],
		[0,0,0,0,0,0,1,1],
		[0,0,1,1,1,0,1,0],
		[0,0,0,0,0,0,1,0],
		[0,1,1,1,1,0,1,0],
		[0,1,1,1,1,0,1,0],
		[0,1,1,1,1,0,1,0],
		[0,0,0,0,0,0,0,0]])
	head = [1,7]
	target = [3,1]
	next_move(y,head,target)
	
	z = np.array([
		[1,1,1,1,0,0,0,0],
		[0,0,0,0,0,0,1,1],
		[0,0,1,1,1,0,1,0],
		[0,0,0,0,0,0,1,0],
		[0,1,1,1,1,0,1,0],
		[0,1,1,1,1,0,1,0],
		[0,1,1,1,1,0,1,0],
		[0,0,0,0,0,0,0,0]])
	head = [7,7]
	target = [3,1]
	next_move(z,head,target)