import random
from square import *

class MineSweeper:
    def __init__(self):
        self.row, self.col = (8, 8)
        self.board = [[Square() for i in range(self.row)] for j in range(self.col)]
        self.mines = 16
        self.flags = 16

    def place_mines(self, x, y):
        for k in range(self.mines):
            index = random.randint(0, self.num_open())
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j].value == 0:
                        if i < x - 2 or j < y - 2 or i > x + 2 or j > x + 2:
                            if index == 0:
                                self.board[i][j].set_value(-1)
                                index -= 1
                            else:
                                index -= 1


    def assign_nums(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j].value == -1:
                    if i > 0:
                        if self.board[i - 1][j].value >= 0:
                            self.board[i - 1][j].increment()
                    if i < self.row - 1:
                        if self.board[i + 1][j].value >= 0:
                            self.board[i + 1][j].increment()
                    if j > 0:
                        if self.board[i][j - 1].value >= 0:
                            self.board[i][j - 1].increment()
                    if j < self.col - 1:
                        if self.board[i][j + 1].value >= 0:
                            self.board[i][j + 1].increment()
                    if i > 0 and j > 0:
                        if self.board[i - 1][j - 1].value >= 0:
                            self.board[i - 1][j - 1].increment()
                    if i < self.row - 1 and j < self.col - 1:
                        if self.board[i + 1][j + 1].value >= 0:
                            self.board[i + 1][j + 1].increment()
                    if i < self.row - 1 and j > 0:
                        if self.board[i + 1][j - 1].value >= 0:
                            self.board[i + 1][j - 1].increment()
                    if i > 0 and j < self.col - 1:
                        if self.board[i - 1][j + 1].value >= 0:
                            self.board[i - 1][j + 1].increment()

    def is_valid_move(self, x, y):
        if x >= 0 and x < 22 and y >= 0 and y < 22 and self.board[x][y].revealed is False:
            return True
        else:
            return False

    def clear_blanks(self, x, y):
        self.board[x][y].reveal()
        if x > 0:
            if not self.board[x - 1][y].revealed:
                self.board[x - 1][y].reveal()
                if self.board[x - 1][y].value == 0:
                    self.clear_blanks(x - 1, y)
        if x < self.row - 1:
            if not self.board[x + 1][y].revealed:
                self.board[x + 1][y].reveal()
                if self.board[x + 1][y].value == 0:
                    self.clear_blanks(x + 1, y)
        if y > 0:
            if not self.board[x][y - 1].revealed:
                self.board[x][y - 1].reveal()
                if self.board[x][y - 1].value == 0:
                    self.clear_blanks(x, y - 1)
        if y < self.col - 1:
            if not self.board[x][y + 1].revealed:
                self.board[x][y + 1].reveal()
                if self.board[x][y + 1].value == 0:
                    self.clear_blanks(x, y + 1)
        if x > 0 and y > 0:
            if not self.board[x - 1][y - 1].revealed:
                self.board[x - 1][y - 1].reveal()
                if self.board[x - 1][y - 1].value == 0:
                    self.clear_blanks(x - 1, y - 1)
        if x < self.row - 1 and y < self.col - 1:
            if not self.board[x + 1][y + 1].revealed:
                self.board[x + 1][y + 1].reveal()
                if self.board[x + 1][y + 1].value == 0:
                    self.clear_blanks(x + 1, y + 1)
        if x < self.row - 1 and y > 0:
            if not self.board[x + 1][y - 1].revealed:
                self.board[x + 1][y - 1].reveal()
                if self.board[x + 1][y - 1].value == 0:
                    self.clear_blanks(x + 1, y - 1)
        if x > 0 and y < self.col - 1:
            if not self.board[x - 1][y + 1].revealed:
                self.board[x - 1][y + 1].reveal()
                if self.board[x - 1][y + 1].value == 0:
                    self.clear_blanks(x - 1, y + 1)



    def make_move(self):
        ans = int(input("Do you want to (0) place a flag or (1) reveal a square: "))
        cord = self.get_input()
        if ans == 0:
            self.board[cord[0]][cord[1]].switch_flag()
        else:
            if self.board[cord[0]][cord[1]].flagged:
                print("Not a valid input try again")
                cord = self.get_input()
            self.board[cord[0]][cord[1]].reveal()
            if self.board[cord[0]][cord[1]].value == 0:
                self.clear_blanks(cord[0], cord[1])
            if self.board[cord[0]][cord[1]].value == -1:
                return "L"
            if self.num_open() == 0:
                return "W"
        return "N"


    def make_first_move(self):
        cord = self.get_input()
        self.board[cord[0]][cord[1]].reveal()
        self.place_mines(cord[0], cord[1])
        self.assign_nums()
        self.clear_blanks(cord[0], cord[1])


    def get_input(self):
        while(True):
            x = int(input("input the row you want "))
            y = int(input("input the column you want "))
            if self.is_valid_move(x, y) is True:
                return (x, y)
            print("Not a valid input try again")

    def draw_board(self):
        for row in self.board:
            print(row)

    def play_game(self):
        self.draw_board()
        self.make_first_move()
        self.draw_board()
        condition = "N"
        while condition == "N":
            condition = self.make_move()
            self.draw_board()
        if condition == "W":
            print("YOU WIN! :)")
        else:
            print("BOOOM: you blew up")

    def num_open(self):
        num = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j].value >= 0 and self.board[i][j].revealed is False:
                    num += 1
        return num



