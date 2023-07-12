def convert(input_grid):
    if len(input_grid)%4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any([len(row)%3 != 0 for row in input_grid]):
        raise ValueError("Number of input columns is not a multiple of three")
    output = ''
    numbers = len(input_grid[0]) // 3
    columns = len(input_grid) // 4
    
    for j in range(columns):
        for i in range(numbers):
            top = input_grid[0+(4*j)][0+(3*i):3+(3*i)]
            mid = input_grid[1+(4*j)][0+(3*i):3+(3*i)]
            bottom = input_grid[2+(4*j)][0+(3*i):3+(3*i)]
            
            if not '_' in top:
                if mid == '  |':
                    output += '1'
                elif mid == '|_|' and bottom == '  |':
                    output += '4'
                else:
                    output += '?'
                continue
                
            if mid == '|_|' and bottom == '|_|':
                output += '8'
            elif mid == '| |' and bottom == '|_|':
                output += '0'
            elif mid == ' _|' and bottom == '|_ ':
                output += '2'
            elif mid == '|_ ' and bottom == ' _|':
                output += '5'
            elif mid == ' _|' and bottom == ' _|':
                output += '3'
            elif mid == '  |' and bottom == '  |':
                output += '7'
            elif mid == '|_|' and bottom == ' _|':
                output += '9'
            elif mid == '|_ ' and bottom == '|_|':
                output += '6'
            else:
                output += '?'
            
        if j != columns-1:
            output += ','
        
    return output
