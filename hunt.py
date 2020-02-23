from player import Player

class Hunt(Player):

    def __init__(self, board):
        super().__init__(board)
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.current_direction = 0
        self.hits = []

    def change_direction(self):
        if(self.hits):
            self.current_direction += 1
            if(self.current_direction==4):
                self.current_direction = 0
                self.hits.pop(0)

    def try_to_open(self):

        x = self.hits[0][0] + self.directions[self.current_direction][0]
        y = self.hits[0][1] + self.directions[self.current_direction][1]
        
        value, already_opened = self.board.open_field(x, y)
        
        return x, y, value, already_opened
    
    def open_random_field(self):
        already_opened = True
        while(already_opened):
            x, y = self.board.random_field()
            value, already_opened = self.board.open_field(x, y)
        
        hit = (x, y)
        if(value in self.board.ships.keys() and hit not in self.hits):
            self.hits.append(hit)
        
        return x, y, value, already_opened

    def move(self):
        if(self.hits):
            x, y, value, already_opened = self.try_to_open()

            while(x==self.board.board_size or x==-1 or y==self.board.board_size or y==-1 or already_opened):
                self.change_direction()
                if(not self.hits):
                    x, y, value, already_opened = self.open_random_field()
                else:
                    x, y, value, already_opened = self.try_to_open()
            
            self.change_direction()
            
        else:
            x, y, value, already_opened = self.open_random_field()

        hit = (x, y)
        if(value in self.board.ships.keys() and hit not in self.hits and not already_opened):
            self.hits.append(hit)
        