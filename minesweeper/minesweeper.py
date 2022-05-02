import random
from square import *

class MineSweeper:
    def __init__(self):
        row, col = (22, 22)
        self.board = [[Square() for i in range(row)] for j in range(col)]
        self.mines = 100

    def place_mines(self):
        for i in range(self.mines):
            index = random.randint(0, self.num_open())
            for i in self.board:
                for j in i:
                    if j.value == 0 and j.revealed is False:
                        if index == 0:
                            self.board[i][j].set_value(-1)
                        else:
                            index -= 1



    def assign_nums(self):
        for i in self.board:
            for j in i:
                if self.board[i][j].value == -1:
                    if i > 0:
                        if self.board[i - 1][j] >= 0:
                            self.board[i - 1][j] += 1
                    if i < 21:
                        if self.board[i + 1][j] >= 0:
                            self.board[i + 1][j] += 1
                    if j > 0:
                        if self.board[i][j - 1] >= 0:
                            self.board[i][j - 1] += 1
                    if j < 21:
                        if self.board[i][j + 1] >= 0:
                            self.board[i][j + 1] += 1
                    if i > 0 and j > 0:
                        if self.board[i - 1][j - 1] >= 0:
                            self.board[i - 1][j - 1] += 1
                    if i < 21 and j < 21:
                        if self.board[i + 1][j + 1] >= 0:
                            self.board[i + 1][j + 1] += 1
                    if i < 21 and j > 0:
                        if self.board[i + 1][j - 1] >= 0:
                            self.board[i + 1][j - 1] += 1
                    if i > 0 and j < 21:
                        if self.board[i - 1][j + 1] >= 0:
                            self.board[i - 1][j + 1] += 1

    def is_valid_move(self, x, y):
        if x >= 0 and x < 22 and y >= 0 and y < 22 and self.board[x][y].revealed is False and self.board[x][y].flagged is False:
            return True
        else:
            return False

    def clear_blanks(self, x, y):
        if x > 0:
            if self.board[x - 1][y].value == 0 and self.board[x - 1][y].revealed is False:
                self.clear_blanks(x - 1, y)

            self.board[x - 1][y].reveal()
        if x < 21:
            if self.board[x + 1][y].value == 0 and self.board[x + 1][y].revealed is False:
                self.clear_blanks(x + 1, y)
            self.board[x - 1][y].reveal()
        if y > 0:
            if self.board[x][y - 1].value == 0 and self.board[x][y - 1].revealed is False:
                self.clear_blanks(x, y - 1)
            self.board[x - 1][y].reveal()
        if y < 21:
            if self.board[x][y + 1].value == 0 and self.board[x][y + 1].revealed is False:=
                self.clear_blanks(x, y + 1)
            self.board[x - 1][y].reveal()
        if x > 0 and y > 0:
            if self.board[x - 1][y - 1].value == 0 and self.board[x - 1][y - 1].revealed is False:
                self.clear_blanks(x - 1, y - 1)
            self.board[x - 1][y].reveal()
        if x < 21 and y < 21:
            if self.board[x + 1][y + 1].value == 0 and self.board[x + 1][y + 1].revealed is False:
                self.clear_blanks(x + 1, y + 1)
            self.board[x - 1][y].reveal()
        if x < 21 and y > 0:
            if self.board[x + 1][y - 1].value == 0 and self.board[x + 1][y - 1].revealed is False:
                self.clear_blanks(x + 1, y - 1)
            self.board[x - 1][y].reveal()
        if x > 0 and y < 21:
            if self.board[x - 1][y + 1].value == 0 and self.board[x - 1][y + 1].revealed is False:
                self.clear_blanks(x - 1, y + 1)
            self.board[x - 1][y].reveal()


    def make_move(self):
        cord = self.get_input()
        self.board[cord[0]][cord[1]].reveal()

    def make_first_move(self):
        cord = self.get_input



    def get_input(self):
        while(True):
            x = int(input("input the row you want "))
            y = int(input("input the column you want "))
            if self.is_valid_move(x, y) is True:
                return (x, y)
            print("Not a valid input try again")

    def draw_board(self):


    def play_game(self):


    def num_open(self):
        num = 0
        for i in self.board:
            for j in i:
                if j.value == 0 and j.revealed is False:
                    num += 1

        return num



