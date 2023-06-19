def rows(letter):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fillers = letters.index(letter) + 1
    spacer = ' '
    output = []
    for i in range(0, (fillers*2-1)):
        if i < fillers:
            iteration = i
        else:
            iteration = fillers*2-(i+2)
        if i == fillers*2-2 or i == 0:
            output.append(f'{spacer*(fillers-1)}{letters[iteration]}{spacer*(fillers-1)}')
        else:
            output.append(f'{spacer*(fillers-iteration-1)}{letters[iteration]}{spacer*(iteration*2-1)}{letters[iteration]}{spacer*(fillers-iteration-1)}')
    return output
