def is_valid(isbn):
    input = isbn.replace('-', '')
    if len(input) != 10:
        return False
    if input[-1] == 'X':
        try:
            if (int(input[0]) * 10 + int(input[1]) * 9 + int(input[2]) * 8 + int(input[3]) * 7 + int(input[4]) * 6 + int(input[5]) * 5 + int(input[6]) * 4 + int(input[7]) * 3 + int(input[8]) * 2 + 10) % 11 == 0:
                return True
            return False
        except:
            return False
    try:
        if (int(input[0]) * 10 + int(input[1]) * 9 + int(input[2]) * 8 + int(input[3]) * 7 + int(input[4]) * 6 + int(input[5]) * 5 + int(input[6]) * 4 + int(input[7]) * 3 + int(input[8]) * 2 + int(input[9])) % 11 == 0:
            return True
        return False
    except:
        return False
