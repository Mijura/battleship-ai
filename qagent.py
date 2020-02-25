from player import Player
from board import Board
import numpy as np
import pandas as pd
import random

class Qagent(Player):

    def __init__(self, board):
        super().__init__(board)
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.qtable = pd.DataFrame(np.zeros((10, 10)), dtype='int') #tabela nagrada
        self.random_explore = 0.8 #procenat za nasumicno gadjanje (smanjuje se tokom igranja)
    
    def find_coord_with_reward(self, reward):
        for i in range (0, len(self.qtable)):
            for j in range (0, len(self.qtable[i])):
                if(self.qtable[i][j]==reward):
                    return i, j

    def update_table(self, x, y, value):
        self.qtable[x][y] = -1 
        if(value in self.board.ships.keys()): #ukoliko je doslo do pogotka obilazi okolne pozicije i dodeljuje im nagradu
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if(new_x < self.board.board_size and new_y < self.board.board_size 
                    and new_x > -1 and new_y > -1 and self.qtable[new_x][new_y]!=-1):
                    self.qtable[new_x][new_y]=5

    def move(self):
        max_reward = self.qtable.max().max() #pronalazak polja sa najvecom nagradom u tabeli nagrada
 
        if(self.random_explore>0):#smanjivanje nasumicnog gadjanja
            self.random_explore -= 0.1

        if(max_reward==0 or random.random() < self.random_explore):
            x, y, value, already_opened = self.get_random_field()
        else:
            x, y = self.find_coord_with_reward(max_reward)
            value, already_opened = self.board.open_field(x, y)
        self.update_table(x, y, value)