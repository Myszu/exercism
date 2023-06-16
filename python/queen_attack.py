class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        if self.row < 0:
            raise ValueError("row not positive")
        if self.column < 0:
            raise ValueError("column not positive")
        if self.row > 7:
            raise ValueError("row not on board")
        if self.column > 7:
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if any([self.diagonal_one(another_queen), self.diagonal_two(another_queen), self.diagonal_three(another_queen), self.diagonal_four(another_queen)]):
            return True
        return False
        
        
    def diagonal_one(self, another_queen):
        r = 0
        c = 0
        while 0 < (self.row + r) <= 7 and 0 < (self.column + c) <= 7:
            r += 1
            c += 1
            if (self.row + r) == another_queen.row and (self.column + c) == another_queen.column:
                return True
        return False
        
        
    def diagonal_two(self, another_queen):
        r = 0
        c = 0
        while 0 < (self.row + r) <= 7 and 0 < (self.column + c) <= 7:
            r += 1
            c -= 1
            if (self.row + r) == another_queen.row and (self.column + c) == another_queen.column:
                return True
        return False
        
        
    def diagonal_three(self, another_queen):
        r = 0
        c = 0
        while 0 < (self.row + r) <= 7 and 0 < (self.column + c) <= 7:
            r -= 1
            c += 1
            if (self.row + r) == another_queen.row and (self.column + c) == another_queen.column:
                return True
        return False
        
        
    def diagonal_four(self, another_queen):
        r = 0
        c = 0
        while 0 < (self.row + r) <= 7 and 0 < (self.column + c) <= 7:
            r -= 1
            c -= 1
            if (self.row + r) == another_queen.row and (self.column + c) == another_queen.column:
                return True
        return False
