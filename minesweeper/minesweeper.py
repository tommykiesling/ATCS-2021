import random
from square import *

class MineSweeper:
    def __init__(self):
        row, col = (22, 22)
        self.board = [[Square() for i in range(row)] for j in range(col)]
        self.mines = 100

    def place_mines(self, x, y):
        for i in range(self.mines):
            index = random.randint(0, self.num_open())
            for i in self.board:
                for j in i:
                    if j.value == 0 and j.revealed is False:
                        if index == 0:
                            self.board[i][j].set_value(-1)
                        else:
                            index -= 1



    def assign_nums(self, ):


    def is_valid_move(self, x, y):
        if x >= 0 and x < 22 and y >= 0 and y < 22 and self.board[x][y].revealed is False:
            return True
        else:
            return False
    def clear_blanks(self):


    def make_move(self):


    def get_input(self):


    def make_first_move(self):


    def draw_board(self):


    def play_game(self):


    def num_open(self):
        num = 0
        for i in self.board:
            for j in i:
                if j.value == 0 and j.revealed is False:
                    num += 1

        return num


