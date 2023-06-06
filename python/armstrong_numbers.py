def is_armstrong_number(number):
    number = str(number)
    digs = len(number)
    summed = 0
    for digit in number:
        summed += int(digit)**digs 
    if int(number) == summed:
        return True
    return False
