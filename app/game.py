import numpy as np

class Game():
    def __init__(self, height, width, game_id):
        self.width = width
        self.height = height
        self.id = game_id
        
        self.board = np.zeros((height,width), dtype=int)
        self.board_e = np.zeros((height,width), dtype=int)
        self.snakes = []
        self.food = []
        
    def parse_data(self, data):
        self.snakes = []
        self.board = np.zeros((self.height,self.width), dtype=int)
        for snake in data["snakes"]:
            if snake["id"] == data["you"]:
                self.snakes.insert(0,snake)
            else:
                self.snakes.append(snake)
        
        self.board = self.parse_board(True)
        self.board_e = self.parse_board(False)
        self.food = data["food"]
        
    def move(self):
        """targets = self.priority_foods()
        board = self.parse_board(self.board)
        min_path = float('inf')
        best_path = []
        for target in targets:
            #path = somewhere.find_path(board, self.snake["coords"][0], target)
            if len(path) < min_path:
                best_path = path
        return best_path[0]"""
        return "down"
    
    def priority_foods(self):
        targets = [] #if empty is returned then no food is available
        for food in self.food:
            min_snake = min([dist(snake["coords"][0],food) for snake in self.snakes[1:]])
            our_dist = dist(self.snakes[0]["coords[0]"],food)
            if our_dist <= min_snake:
                targets.insert(0,food)
        return targets
        
    def parse_board(self, is_us=True):
        board = np.zeros((self.height,self.width), dtype=int)
        for snake in self.snakes:
            for x,y in snake["coords"]:
                board[y,x] = 1
            tail = snake["coords"][-1]
            if snake["health_points"] > 98:
                board[tail[1],tail[0]] = 1

        if is_us:
            length = len(self.snakes[0]["coords"])
            head = self.snakes[0]["coords"][0]
            board[head[1],head[0]] = 0
            for snake in self.snakes[1:]:
                head = snake["coords"][0]
                if length <= len(snake["coords"]):
                    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                        x,y = x+head[0], y+head[1]
                        if x >= 0 and x < self.width and y >= 0 and y < self.height:
                            board[y,x] = 1 
        return board
    
    @staticmethod
    def dist(start, end):
        return abs(start[0]-end[0])+abs(start[1]-end[1])