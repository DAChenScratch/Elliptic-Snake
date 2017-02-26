import numpy as np

class Game():
    def __init__(self, height, width, game_id):
        self.width = width
        self.height = height
        self.id = game_id
        
        self.board = np.zeros((2,height,width), dtype=int)
        self.snakes = []
        self.food = []
        
    def parse_board_data(self, data):
        self.snakes = []
        self.board = np.zeros((2,self.height,self.width), dtype=int)
        for snake in data["snakes"]:
            if snake["id"] == data["you"]:
                self.snakes.insert(0,snake)
            else:
                self.snakes.append(snake)
        
        #0 empty, 1 head, 2 body, 3 tail, 4 food, 5 dead_snake
        for snake_num, snake in enumerate(self.snakes):
            for x,y in snake["coords"]:
                self.board[0,y,x] = 2
                self.board[1,y,x] = snake_num
            head = snake["coords"][0]
            tail = snake["coords"][-1]
            self.board[0,tail[1],tail[0]] = 3
            self.board[0,head[1],head[0]] = 1 
        for food in data["food"]:
            self.board[0,food[1],food[0],] = 4
        self.food = data["food"]
        for dead_snake in data["dead_snakes"]:
            for x,y in dead_snake["coords"]:
                self.board[0,y,x] = 5
        
    def move():
        pass