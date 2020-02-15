import numpy as np
import random as rd

class Board:

    def __init__(self):
        self.board_size = 10

        self.table = self.create_empty_table()
        self.ships = [ {'length': 5, 'id': 'c', 'name': 'Carrier'},
                       {'length': 4, 'id': 'b', 'name': 'Battleship'},
                       {'length': 3, 'id': 'd', 'name': 'Destroyer'},
                       {'length': 3, 'id': 's', 'name': 'Submarine'},
                       {'length': 2, 'id': 'p', 'name': 'Patrol Boat'}]
        
        for board in self.ships:
            self.add_ship(board)

    def create_empty_table(self):
        table = []
        for i in range(0, self.board_size):
            table.append([0]*self.board_size)
        return table

    def is_busy(self, x, y):
        return self.table[x][y] != 0
    
    def is_cross(self, main_coord, secondary_coord, ship_length):
        return False #TODO

    def place_ship(self, main_coord, secondary_coord, ship_id, ship_length):
        for mc in range(main_coord, main_coord + ship_length):
            self.table[mc][secondary_coord] = ship_id

    def add_ship(self, ship):
        placed = False
        while(not placed):
            horizontal = rd.choice([True, False])
            if(horizontal):
                x = rd.randint(0, self.board_size - ship['length'] -1)
                y = rd.randint(0, self.board_size - 1)
                if(not self.is_busy(x, y) and not self.is_cross( x, y, ship['length'])):
                    self.place_ship(x, y, ship['id'], ship['length'])
                    placed = True
            else:
                x = rd.randint(0, self.board_size - 1)
                y = rd.randint(0, self.board_size - ship['length'] -1)
                if(not self.is_busy(x, y) and not self.is_cross( y, x, ship['length'])):
                    self.place_ship(y, x, ship['id'], ship['length'])
                    placed = True

board = Board()
for row in board.table:
    print(row)