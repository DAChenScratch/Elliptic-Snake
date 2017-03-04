import numpy as np
import networkx as nx


def next_move(board, head, target):
	G = nx.Graph()
	for i in range((len(board)*len(board[0]))):
		G.add_node(i)
	
	for i in range((len(board)*len(board[0]))):
		#1 is try right
		#2 is try left
		#3 is try up
		#4 is try down
		for j in range(1,5):
			if j == 1:
				#stay on the board
				if(i+j)%len(board[0]) == 0:
					continue
				if (board[int()((i+j)/board[0])]][(i+j)%board[0]]) == 0:
					G.add_edge(i,j)
			if j == 2:
				if i%len(board[0]) == 0:
					continue
				if (board[int()((i-1)/board[0])]][(i-1)%board[0]]) == 0:
					G.add_edge(i,j)
			if j == 3:
				if i< len(board[0]):
					continue
				if (board[int()((i-len(board[0])/board[0])]][(i-len(board[0])%board[0]]) == 0:
					G.add_edge(i,j)
			if j == 4:
				if i/len(board[0]) == len(board)-1:
					continue
				if (board[int()((i+len(board[0])/board[0])]][(i+len(board[0])%board[0]]) == 0:
					G.add_edge(i,j)
		#done making graph G. now find a path and hope this works...
		
		path = nx.shortest_path(G,source=((head[0]*len(board[0]))+(head[1]*len(board))),target=((target[0]*len(board[0]))+(target[1]*len(board)))
		return path