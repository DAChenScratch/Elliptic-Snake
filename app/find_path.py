import numpy as np
import networkx as nx

def find_path(board, head, target):
    height, width = board.shape
    G = nx.Graph()
    for i in range(height*width):
        G.add_node(i)
    for x,y in np.ndenumerate(board):
        for a,b in [(1,0),(-1,0),(0,1),(1,0)]:
            a = x+a
            b = y+b
            if a >= 0 and a < width and b >= 0 and b < height:
                if board[y,x] == 0 and board[b,a] == 0:
                    G.add_edge(y*width+x,b*width+a)
    
    path = nx.shortest_path(G,source=(head[1]*width+head[0]),target=(target[1]*width+target[0]))
    print(path)
    
if __name__ == "__main__":
	x = np.array([
        [0,0,0,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,1,0,0]])
	head = [2,3]
	target = [0,0]
	find_path(x,head,target)
	
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
	find_path(y,head,target)
	
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
	find_path(z,head,target)