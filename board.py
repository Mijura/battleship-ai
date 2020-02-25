import numpy as np
import random as rd

class Board:

    def __init__(self):
        self.board_size = 10

        self.table = self.create_empty_table()
        self.opened = [] #lista za smestanje otvorenih polja
        self.ships = {
            'c': {'length': 5, 'name': 'Carrier'},
            'b': {'length': 4, 'name': 'Battleship'},
            'd': {'length': 3, 'name': 'Destroyer'},
            's': {'length': 3, 'name': 'Submarine'},
            'p': {'length': 2, 'name': 'Patrol Boat'}
        }

        for id, ship in self.ships.items(): #dodavanje brodova na praznu tablu
            self.add_ship(id, ship)

    def create_empty_table(self):
        table = []
        for i in range(0, self.board_size):
            table.append([0]*self.board_size)
        return table
    
    #proverava da li brod moze da se postavi na kordinate (u zadatom pravcu) a da pri tome ne dodje do ukrstanja sa drugim brodom
    def is_cross(self, x, y, ship_length, horizontal): 
        if (horizontal): #provera da li brod moze da se postavi horizontalno
            for i in range(x, x + ship_length):
                if (self.table[i][y] != 0): 
                    return True
        else: #provera da li brod moze da se postavi vertikalno
            for i in range(y, y + ship_length):
                if (self.table[x][i] != 0):
                    return True

        return False

    def place_ship(self, x, y, ship_id, ship_length, horizontal): #postavlja brod u zadatom pravcu
        if (horizontal):
            for i in range(x, x + ship_length):
                self.table[i][y] = ship_id
        else:
            for i in range(y, y + ship_length):
                self.table[x][i] = ship_id

    def add_ship(self, id, ship): #postavlja brod na tablu
        placed = False
        while(not placed): #ponavlja proces dok ne postavi brod (zbog ukrstanja sa vec postavljenim brodom)
            horizontal = rd.choice([True, False]) #random bira pravac
            if(horizontal):
                x = rd.randint(0, self.board_size - ship['length'] -1)
                y = rd.randint(0, self.board_size - 1)
            else:
                x = rd.randint(0, self.board_size - 1)
                y = rd.randint(0, self.board_size - ship['length'] -1)
            
            #ukoliko nije doslo do ukrstanja sa vec postavljenim brodom
            if(not self.is_cross(x, y, ship['length'], horizontal)):
                self.place_ship(x, y, id, ship['length'], horizontal)
                placed = True

    #otvaranje polja na zadatim koordinatama
    def open_field(self, x, y):
        if (x==self.board_size or y==self.board_size or x==-1 or y==-1): #ukoliko su koordinate van okvira tabele
            return None, None

        field_value = self.table[x][y]

        coord = (x, y)
        already_opened = coord in self.opened  #provera da li je polje vec otvorano

        if(not already_opened):
            self.opened.append(coord)
            if(field_value!=0):
                print("pogodak " + str (x) +" " +str(y) + " " +str(field_value))
                self.ships[field_value]['length'] -= 1

        return field_value, already_opened

    def remaining_targets(self): #vraca koliko ima jos neotkrivenih delova brodova
        count = 0
        for k, v in self.ships.items():
            count += v['length']
        return count

    def random_field(self): #generise random koordinate u okviru table
        x = rd.randint(0, self.board_size - 1)
        y = rd.randint(0, self.board_size - 1)
        return x, y