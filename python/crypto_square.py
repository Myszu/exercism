import re
def cipher_text(plain_text):
    normalized = re.sub('[ !@#$%^&*,.\+\-\=]', '', plain_text).lower()
    chars = len(normalized)
    columns = 1
    for i in range(chars):
        if i > columns: columns = i
        if i*(i-1) >= chars:
            normalized += ' '*abs((columns * (columns - 1))-chars)
            break
        elif i*i >= chars:
            normalized += ' '*abs((columns * columns)-chars)
            break
    cipher = ['']
    for i, letter in enumerate(normalized):
        try:
            cipher[i%columns] += letter
        except IndexError:
            cipher.append(letter)
    return ' '.join(cipher)
