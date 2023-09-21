#8-queen
class Board:
    def __init__(self) :
        self.board = [["_" for _ in range (8)] for _ in range(8)]
         
    def __repr__(self):
         res =""
         for row in self.board:
            for col in row:
                res+=col
                res+= " "
            res+= "\n" 
         return res

    def is_legal_row(self,row,col):
        for j in range(len(self.board)):
            if self.board[row][j] == "Q":
                return False
        return True

    def is_legal_col(self,row,col):
        for i in range(len(self.board)):
            if self.board[i][col] == "Q":
                return False
        return True
 
    def is_on_board (self,row,col):
        return row>=0 and row<8 and col>=0 and col<8

    def is_legal_diag(self,row,col):
         for i in range(len(self.board)):
             if self.is_on_board(row -i, col -i) and self.board[row-i][col-i] == "Q":
                return False
             if self.is_on_board(row -i, col +i) and self.board[row-i][col+i] == "Q":
                return False
             if self.is_on_board(row +i, col -i) and self.board[row+i][col-i] == "Q":
                return False
             if self.is_on_board(row +i, col +i) and self.board[row+i][col+i] == "Q":
                 return False
         return True

    def is_legal(self, row, col):
        if not self.is_legal_row(row,col):
             return False
        if not self.is_legal_col(row,col):
             return False
        if not self.is_legal_diag(row,col):
            return False
        return True

    def set_queen_at (self,row,col):
        self.board[row][col] = "Q"

    def unset_queen_on(self,row):
         self.board[row] = ["_" for _ in range(8)]

    def get_queen_on(self,row):
        for col in range(len(self.board)):
            if self.board[row][col] == "Q":
                return col
        raise ValueError("programmer error")
 
    def search(self):
        row = 0
        col = 0
        nsol = 0
        while row >=0 :
            if row < 8: # check if need backtracking
                if col >= 8:
                    row -=1
                    if row >= 0:
                        col = self.get_queen_on(row)+1
                        self.unset_queen_on(row)
                    col = self.get_queen_on(row-1)
                    self.unset_queen_on(row-1)
                    col += 1
                    row -= 1  # can cause error when row = 0
                else:
                    if self.is_legal(row,col):
                        self.set_queen_at(row,col)
                        row += 1
                        col = 0
                    else:
                        col += 1
                   
            else:
                nsol += 1
                print("find a solution number", nsol)
                print(self)
                row -=1     # only do this backtracking if we in while loop
                col = self.get_queen_on(row)+1
                self.unset_queen_on(row) 
                
        print("find none of solutions")
        
my_board = Board()
print(my_board)
#my_board.search()