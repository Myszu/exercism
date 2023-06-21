def resistor_label(colors):
    if len(colors) > 3:
        r =''
        for color in colors[:-2]:
            r += f'{assign(color)}'
        r = int(r)*resistance(colors[-2])
        return prefix(r) + f' ±{suffix(assign(colors[-1]))}'
    elif len(colors) > 2:
        r = int(f"{int(f'{assign(colors[0])}{assign(colors[1])}')*resistance(colors[2])}")
        return prefix(r)
    return prefix(assign(colors[0]))
  

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
        'white',
        'gold',
        'silver'
    ]
    if color in table:
        return table.index(color)
    

def resistance(color):
    return 10**(assign(color))
    

def prefix(r):
    if r >= 1000000000:
        if r % 1000000000 == 0:
            return f'{r // 1000000000} gigaohms'
        return f'{r / 1000000000} gigaohms'
    if r >= 1000000:
        if r & 1000000 == 0:
            return f'{r // 1000000} megaohms'
        return f'{r / 1000000} megaohms'
    if r >= 1000:
        if r % 1000 == 0:
            return f'{r // 1000} kiloohms'
        return f'{r / 1000} kiloohms'
    return f'{r} ohms'


def suffix(t):
    tolerances = ['', '1%', '2%', '', '', '0.5%', '0.25%', '0.1%', '0.05%', '', '5%', '10%']
    return tolerances[t]
