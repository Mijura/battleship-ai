from abc import ABC, abstractmethod
from board import Board

class Player(ABC):

    def __init__(self, board):
        self.board = board

    @abstractmethod
    def move(self):
        pass
        