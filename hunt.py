from player import Player

class Hunt(Player):

    def __init__(self, board):
        super().__init__(board)
        self.main_hit = None
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.last_shot = None
        self.current_direction = 0
    
    def move(self):
        if(self.main_hit is None):
            x, y = self.board.random_field()
            value, previous_opened = self.board.open_field(x, y)
            while(not previous_opened):
                x, y = self.board.random_field()
                value, previous_opened = self.board.open_field(x, y)
            
            if(value!=0):
                self.main_hit = (x, y)
                self.last_shot = (x, y)

        else:
            #TODO GRANICE PROVERITI!
            if (self.main_hit[0]==self.board.board_size-1 or self.main_hit[1]==self.board.board_size-1):
                self.last_shot = self.main_hit
                self.current_direction += 1

            x = self.last_shot[0] + self.directions[self.current_direction][0]
            y = self.last_shot[1] + self.directions[self.current_direction][1]
            
            value, opened = self.board.open_field(x, y)
            self.last_shot = (x, y)

            if(value==0):
                self.current_direction += 1
                self.last_shot = self.main_hit
                if(self.current_direction==4):
                    self.current_direction = 0
                    self.main_hit = None
                    self.last_shot = None