base = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

suffixes = {
    0: 'thousand',
    1: 'million',
    2: 'billion'
}

def say(number: int, iteration: int = 0):
    if not 0 <= number <= 999999999999:
        raise ValueError("input out of range")
    if number < 20:
        return base.get(number)
    if number < 100:
        first = int(str(number)[0])
        second = int(str(number)[1])
        if number % 10 == 0:
            return f'{tens.get(first)}'
        return f'{tens.get(first)}-{base.get(second)}'
    if number % 1000000000 == 0:
        return f'{say(number//1000000000)} {suffixes[2]}'
    if number % 1000000 == 0:
        return f'{say(number//1000000)} {suffixes[1]}'
    if number < 1000:
        return (f'{base.get(number//100)} hundred {say(number%100) if number%100 > 0 else ""}').strip()
    return (f'{say(number//1000, iteration+1)} {suffixes[iteration]} {say(number%1000) if number%1000 > 0 else ""}').strip()
