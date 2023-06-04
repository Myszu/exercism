def value(colors):
    return int(f'{assign(colors[0])}{assign(colors[1])}')

def assign(color):
    table = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
    if color in table:
        return table.index(color)
