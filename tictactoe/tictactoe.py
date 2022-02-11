import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        row, col = (3, 3)
        self.board = [['-' for i in range(row)] for j in range(col)]


    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Place X's and O's until a tie or someone gets three in a row" )
        return

    def print_board(self):
        for row in self.board:
            print(row)
        return

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row <= 2 and col <= 2:
            return self.board[row][col] == '-'
        return False


    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        while(True):
            rowcord = int(input("input the row you want "))
            colcord = int(input("input the column you want "))
            if self.is_valid_move(rowcord, colcord) is True:
                self.place_player(player, rowcord, colcord)
                return
            print("Not a valid input try again")

        return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        self.take_random_turn(player)
        return

    def check_col_win(self, player):
        # TODO: Check col win
        if self.board[0][0] == player and self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return True
        if self.board[0][1] == player and self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return True
        if self.board[0][2] == player and self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return True

        return False

    def check_row_win(self, player):
        # TODO: Check row win
        if self.board[0][0] == player and self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return True
        if self.board[1][0] == player and self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return True
        if self.board[2][0] == player and self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[1][1] == player:
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_row_win(player) is True:
            print("row win")
            return True
        if self.check_col_win(player) is True:
            print("col win")
            return True
        if self.check_diag_win(player) is True:
            print("diag win")
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        for row in self.board:
            for x in row:
                if x == '-':
                    return False

        return True

    def play_game(self):
        # TODO: Play game
        player = 'X'
        self.print_instructions()
        self.print_board()
        while(True):
            print("")
            self.take_turn(player)
            self.print_board()
            if self.check_win(player) is True:
                print("player " + player + " wins")
                return
            if self.check_tie() is True:
                print("Its a tie")
                return
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        return

    def take_random_turn(self, player):
        while (True):
          row = random.randint(0, 2)
          col = random.randint(0, 2)
          if self.is_valid_move(row, col) is True:
              self.place_player(player, row, col)
              return



