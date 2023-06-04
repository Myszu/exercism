def color_code(color):
    cols = colors()
    if color in cols:
        return cols.index(color)


def colors():
    colors_list = [
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
    return colors_list
