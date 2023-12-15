def spiral_matrix(size):
    matrix = [[0 for x in range(size)] for y in range(size)]
    row_start = 0
    row_end = size
    column_start = 0
    column_end = size
    number = 1

    while number <= size**2:
        for column in range(column_start, column_end):
            matrix[row_start][column] = number
            number += 1 
            
        for row in range(row_start+1, row_end):
            matrix[row][column_end-1] = number
            number += 1

        for column in range(column_end-2, column_start-1, -1):
            matrix[row_end-1][column] = number
            number += 1

        for row in range(row_end-2, row_start, -1):
            matrix[row][column_start] = number
            number += 1

        row_start += 1
        row_end -= 1
        column_start += 1
        column_end -= 1
        
    return matrix