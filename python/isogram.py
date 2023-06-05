def is_isogram(string):
    output = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in string.lower():
        if letter in output:
            return False
        if letters.find(letter) >= 0:
            output.append(letter)
    return True
