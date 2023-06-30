def primes(limit):
    numbers = [number for number in range(2, limit+1)]
    for number in numbers:
        for digit in range(number, limit+1):
            if digit%number == 0 and digit != number:
                try:
                    numbers.remove(digit)
                except ValueError:
                    continue
    return numbers
