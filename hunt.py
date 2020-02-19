from player import Player

class Hunt(Player):

    def __init__(self, board):
        super().__init__(board)
        self.main_hit = None
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.last_shot = None
        self.current_direction = 0

    def reset_all(self):
        self.current_direction = 0
        self.main_hit = None
        self.last_shot = None

    def change_direction(self):
        self.current_direction += 1
        self.last_shot = self.main_hit
        if(self.current_direction==4):
            self.reset_all()

    def try_to_open(self):

        if(self.main_hit is None):
            self.open_random_field()

        x = self.last_shot[0] + self.directions[self.current_direction][0]
        y = self.last_shot[1] + self.directions[self.current_direction][1]
            
        value, opened = self.board.open_field(x, y)
        self.last_shot = (x, y)
        return x, y, value, opened
    
    def open_random_field(self):
        x, y = self.board.random_field()
        value, previous_opened = self.board.open_field(x, y)
        while(not previous_opened):
            x, y = self.board.random_field()
            value, previous_opened = self.board.open_field(x, y)
            
        if(value!=0):
            self.main_hit = (x, y)
            self.last_shot = (x, y)

    def move(self):
        x, y, value, opened = self.try_to_open()
        while(x==self.board.board_size or x==-1 or y==self.board.board_size or y==-1):
            self.change_direction()
            x, y, value, opened = self.try_to_open()
        if(value==0):
            self.change_direction()