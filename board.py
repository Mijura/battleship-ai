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
    
    def is_cross(self, x, y, ship_length, horizontal):
        if (horizontal):
            for i in range(x, x + ship_length):
                if (self.table[i][y] != 0):
                    return True
        else:
            for i in range(y, y + ship_length):
                if (self.table[x][i] != 0):
                    return True

        return False

    def place_ship(self, x, y, ship_id, ship_length, horizontal):
        if (horizontal):
            for i in range(x, x + ship_length):
                self.table[i][y] = ship_id
        else:
            for i in range(y, y + ship_length):
                self.table[x][i] = ship_id

    def add_ship(self, ship):
        placed = False
        while(not placed):
            horizontal = rd.choice([True, False])
            if(horizontal):
                x = rd.randint(0, self.board_size - ship['length'] -1)
                y = rd.randint(0, self.board_size - 1)
            else:
                x = rd.randint(0, self.board_size - 1)
                y = rd.randint(0, self.board_size - ship['length'] -1)
            
            if(not self.is_busy(x, y) and not self.is_cross(x, y, ship['length'], horizontal)):
                self.place_ship(x, y, ship['id'], ship['length'], horizontal)
                placed = True
