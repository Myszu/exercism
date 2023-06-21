class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = matrix_string.split('\n')

    
    def row(self, index):
        return list(map(int, self.matrix[index-1].split()))

  
    def column(self, index):
        output = [int(row.split()[index-1]) for row in self.matrix]
        return output
