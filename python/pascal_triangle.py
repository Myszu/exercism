def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    
    *numbers, last = rows(row_count-1)
    new = [x + y for x, y in zip(last + [0], [0] + last)]
    return [*numbers, last, new]
