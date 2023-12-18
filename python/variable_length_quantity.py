def encode(numbers):
    output = []
    
    for number in reversed(numbers):
        first = True
        
        while number > 0 or first:
            output.append(number % 128 if first else number % 128 + 128)
            number //= 128
            first = False
            
    output.reverse()
    return output
          

def decode(bytes_):
    output = []
    number = 0
    
    for byte in bytes_:
        number *= 128
        number += (byte % 128)
        
        if byte < 128:
            output.append(number)
            number = 0
            
    if number > 0 or len(output) == 0:
        raise ValueError("incomplete sequence")
    
    return output