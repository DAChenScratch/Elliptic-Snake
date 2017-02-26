import numpy as np

class Game():
    num_instances = 0
    def __init__(self, height, width, game_id):
        self.width = width
        self.height = height
        self.game_id = game_id
        
        self.board = np.zeros((2,height,width))
        self.snakes = []
        
    def parse_board_data(self, data):
        self.snakes = []
        self.board = np.zeros((2,self.height,self.width))
        for snake in data["snakes"]:
            if snake["id"] == data["you"]:
                self.snakes.insert(0,snake)
            else:
                self.append(snakes)
        
        #0 empty, 1 head, 2 body, 3 tail, 4 food, 5 dead_snake
        for snake_num, snake in enumerate(snakes):
            for x,y in snake["coords"]:
                self.board[0,y,x] = 2
                self.board[1,y,x] = snake_num
            head = snake["coords"][0]
            tail = snake["coords"][-1]
            self.board[0,head[1],head[0]] = 1 
            self.board[0,tail[1],tail[0]] = 3
        for food in data["food"]:
            self.board[0,food[1],food[2],] = 4
        for dead_snake in data["dead_snakes"]:
            self.board[0,y,x] = 5
        
    def move():
        pass