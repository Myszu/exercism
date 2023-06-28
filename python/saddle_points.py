def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')
    
    max_row = list(map(max, matrix))
    min_col = list(map(min, list(zip(*matrix))))
    
    return [{'row': row+1, 'column': column+1} for row, rows in enumerate(max_row) for column, columns in enumerate(min_col) if rows == columns]
