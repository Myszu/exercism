import re
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cypher = alphabet[::-1]

def encode(plain_text):
    plain_text = re.sub('[ !@#$%^&*.,]', '', plain_text)
    output = ''
    chars = 0
    
    for letter in plain_text:
        if letter.lower() in alphabet:
            output += cypher[alphabet.index(letter.lower())]
        else:
            output += letter.lower()
        chars += 1
        if chars%5 == 0 and chars > 0:
            output += ' '
            chars = 0
    return output.strip()


def decode(ciphered_text):
    despaced = ciphered_text.replace(' ', '')
    output = ''
    
    for letter in despaced:
        if letter.lower() in alphabet:
            output += cypher[alphabet.index(letter.lower())]
        else:
            output += letter.lower()
    return output
