from player import Player
from board import Board
import numpy as np
import pandas as pd
import random

class Qagent(Player):

    def __init__(self, board, learning_rate, discount):
        super().__init__(board)
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.qtable = pd.DataFrame(np.zeros((10, 10)), dtype='int')
        self.random_explore = 0.8
        self.count = 0

        self.learning_rate = learning_rate
        self.discount = discount
    
    def find_coord_with_reward(self, reward):
        for i in range (0, len(self.qtable)):
            for j in range (0, len(self.qtable[i])):
                if(self.qtable[i][j]==reward):
                    return i, j

    def get_maximum_expected_future_reward(self, x, y):
        rewards = []
        rewards.append(0)
        for direction in self.directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if(new_x < self.board.board_size and new_y < self.board.board_size 
                    and new_x > -1 and new_y > -1 and self.qtable[new_x][new_y]!=-1):
                        reward = self.qtable[new_x][new_y]
                        if(reward>0):
                            rewards.append(reward)
        return max(rewards)

    def update_table(self, x, y, value):
        self.qtable[x][y] = -1 
        if(value in self.board.ships.keys()):
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if(new_x < self.board.board_size and new_y < self.board.board_size 
                    and new_x > -1 and new_y > -1 and self.qtable[new_x][new_y]!=-1):
                    current_value = self.qtable[new_x][new_y]
                    learned_value = 10 + self.discount * self.get_maximum_expected_future_reward(new_x, new_y)
                    self.qtable[new_x][new_y] = (1 - self.learning_rate) * current_value + self.learning_rate * learned_value

    def move(self):
        max_reward = self.qtable.max().max()
 
        if(self.random_explore>0):
            self.random_explore -= 0.1

        if(max_reward==0 or random.random() < self.random_explore):
            x, y, value, already_opened = self.get_random_field()
        else:
            x, y = self.find_coord_with_reward(max_reward)
            value, already_opened = self.board.open_field(x, y)
        self.update_table(x, y, value)