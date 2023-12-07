def egg_count(display_value):
    binary = to_binary(display_value)
    return sum(binary)
    

def to_binary(number):
    output = []
    full = number//2
    reminder = number%2
    output.append(reminder)
    
    if full > 0:
        recurr = to_binary(full)
        output.extend(recurr)
    return output
