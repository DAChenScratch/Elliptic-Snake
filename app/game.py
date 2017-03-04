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
        
    def move(self):
        targets = self.priority_foods()
        board = self.parse_board(self.board)
        min_path = float('inf')
        best_path = []
        for target in targets:
            path = somewhere.find_path(board, self.snake["coords"][0], target)
            if len(path) < min_path:
                best_path = path
        return best_path[0]
    
    def priority_foods(self):
        targets = [] #if empty is returned then no food is available
        for food in self.food:
            min_snake = min([dist(snake["coords"][0],food) for snake in self.snakes[1:]])
            our_dist = dist(self.snakes[0]["coords[0]"],food)
            if our_dist <= min_snake:
                targets.insert(0,food)
        return targets
        
    def parse_board(self):
        board = np.zeros((2,height,width), dtype=int)
        for x in range(self.width):
            for y in range(self.height):
                if self.board[0,y,x] in [1,2,5]:
                    board[y,x] = 1
        for snake in self.snakes[1:]:
            head = snake["coords"][0]
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                x += head[0]
                y += head[1]
                if x >= 0 and x < self.width and y >= 0 and y < self.height:
                    if len(snake["coords"]) >= len(self.snake["coords"]):
                        board[y,x] = 1
                    if self.board[y,x] == 4 or snake["health"] > 97:
                        tail = snake["coords"][-1]
                        board[tail[1],tail[0]] = 1
        return board
    
    @staticmethod
    def dist(start, end):
        return abs(start[0]-end[0])+abs(start[1]-end[1])