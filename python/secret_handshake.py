def commands(binary_str):
    output = []
    binary_str = binary_str[::-1]
    for i, number in enumerate(binary_str):
        if i == 0 and int(number):
            output.append('wink')
            continue
        if i == 1 and int(number):
            output.append('double blink')
            continue
        if i == 2 and int(number):
            output.append('close your eyes')
            continue
        if i == 3 and int(number):
            output.append('jump')
            continue        
    if int(binary_str[-1]):
        output = output[::-1]
    return output
