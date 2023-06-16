def decode(string):
    output = ''
    qty = 1
    prev = False
    for sign in string:
        if sign.isnumeric():
            if prev:
                qty = int(str(qty) + sign)
            else:
                qty = int(sign)
            prev = True
            continue
        prev = False
        output += (sign*qty)
        qty = 1
    return output
            

def encode(string):
    buffer = ''
    count = 0
    output = ''
    for sign in string:
        if buffer == sign:
            count += 1
            continue
        elif buffer != sign and buffer != '':
            if count > 1:
                output += str(count) + buffer
            else:
                output += buffer
            count = 1
        else:
            count += 1
        buffer = sign
    if count > 1:
        output += str(count) + buffer
    else:
        output += buffer
    return output
