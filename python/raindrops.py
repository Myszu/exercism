def convert(number):
    sound = ''
    if number % 3 == 0:
        sound = sound + 'Pling'
    if number % 5 == 0:
        sound = sound + 'Plang'
    if number % 7 == 0:
        sound = sound + 'Plong'
    if not sound:
        return str(number)
    return sound
