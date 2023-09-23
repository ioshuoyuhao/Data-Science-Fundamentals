import os
# this is the last version of the 8 queens problem which is optimized in lecture 3.
class Board:

    def __init__(self):
        self.queen = "Q"
        self.blank = "_"
        self.board = [[self.blank for _ in range(8)] for _ in range(8)]

    def __repr__(self):
        res = ""
        for row in self.board:
            for col in row:
                res += col
                res += " "
            res += "\n"
        return res

    def is_queen(self, row, col):
        return self.board[row][col] == self.queen

    def is_legal_row(self, row, col):
        for j in range(len(self.board)):
            if self.is_queen(row, j):
                return False
        return True
    
    def is_legal_col(self, row, col):
        for i in range(len(self.board)):
            if self.is_queen(i, col):
                return False
        return True
    
    def is_on_board(self, row, col):
        return row >= 0 and row < 8 and col >= 0 and col < 8

    def is_legal_diag(self, row, col):
        for i in range(len(self.board)):
            if self.is_on_board(row - i, col - i) and self.is_queen(row - i, col - i):
                return False
            if self.is_on_board(row - i, col + i) and self.is_queen(row - i, col + i):
                return False
            if self.is_on_board(row + i, col - i) and self.is_queen(row + i, col - i):
                return False
            if self.is_on_board(row + i, col + i) and self.is_queen(row + i, col + i):
                return False
        return True
    
    def is_legal(self, row, col):
        if not self.is_legal_row(row, col):
            return False
        if not self.is_legal_col(row, col):
            return False
        if not self.is_legal_diag(row, col):
            return False
        return True

    def set_queen_at(self, row, col):
        self.board[row][col] = self.queen
    
    def unset_queen_on(self, row):
        self.board[row] = [self.blank for _ in range(8)]

    def get_queen_on(self, row):
        for col in range(len(self.board)):
            if self.is_queen(row, col):
                return col
        raise ValueError("programmer error")

    def search(self):
        row = 0
        col = 0
        nsols = 0
        
        while row >= 0:
            if row < 8:
                if col >= 8:
                    row -= 1
                    if row >= 0:
                        col = self.get_queen_on(row) + 1
                        self.unset_queen_on(row)
                else:
                    if self.is_legal(row, col):
                        self.set_queen_at(row, col)
                        row += 1
                        col = 0
                    else:
                        col += 1

            else:
                nsols += 1
                print("found solution number ", nsols)
                print(self)
                input("Enter for next solutions: ")
                os.system("clear")
                row -= 1
                col = self.get_queen_on(row) + 1
                self.unset_queen_on(row)

        print("no more solutions")
    
my_board = Board()
my_board.search()