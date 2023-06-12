def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    
    for letter in text:
        if letter in alphabet:
            target = shift(alphabet.index(letter) + key)
            output += alphabet[target]
        elif letter in alphabet.upper():
            target = shift(alphabet.upper().index(letter) + key)
            output += alphabet.upper()[target]
        else:
            output += letter
    return output
    
    
def shift(target):
    if target >= 26:
        return target - 26
    return target
