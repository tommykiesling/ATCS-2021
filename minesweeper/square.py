
class Square:

    def __init__(self):
        # value represents the number of flags around a square, -1 means its a mine
        self.value = 0
        self.revealed = False
        self.flagged = False
        self.first_square = False

    def set_value(self, val):
        self.value = val

    def switch_flag(self):
        if not self.flagged:
            self.flagged = True
        else:
            self.flagged = False

    def reveal(self):
        self.revealed = True

    def set_first_square(self):
        self.first_square = True



