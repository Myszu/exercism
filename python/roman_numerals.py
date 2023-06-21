def roman(number):
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman   = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    output = []
    
    while (number > 0):
        for i, digit in enumerate(arabic):
            if (number >= digit):
                output.append(roman[i])
                number -= digit
                break
    return ''.join(output)
