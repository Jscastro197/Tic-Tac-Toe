import math
import time


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def winner(self, square, letter):
        # checking the row
        row_index = math.floor(square / 3)
        row = self.board[row_index * 3:(row_index + 1) * 3]
        if all([s == letter for s in row]):
            return True
        # checking column
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False
