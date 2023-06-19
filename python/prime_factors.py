def factors(value):
    primes = []
    buffer = 2
    while value != 1:
        if value % buffer == 0:
            primes.append(buffer)
            value /= buffer
        else:
            buffer += 1
    return primes
