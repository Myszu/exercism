def label(colors):
    r = int(f"{int(f'{assign(colors[0])}{assign(colors[1])}')*resistance(colors[2])}")
    converted = prefix(r)
    return converted
  

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
    

def resistance(color):
    return 10**(assign(color))
    

def prefix(r):
    if r >= 1000000000:
        r /= 1000000000
        return f'{int(r)} gigaohms'
    if r >= 1000000:
        r /= 1000000
        return f'{int(r)} megaohms'
    if r >= 1000:
        r /= 1000
        return f'{int(r)} kiloohms'
    return f'{int(r)} ohms'
