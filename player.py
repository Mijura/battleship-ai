from abc import ABC, abstractmethod
from board import Board

class Player(ABC):

    def __init__(self, board):
        self.board = board

    def get_random_field(self):
        already_opened = True
        while(already_opened):
            x, y = self.board.random_field()
            value, already_opened = self.board.open_field(x, y)
        return x, y, value, already_opened

    @abstractmethod
    def move(self):
        pass
        