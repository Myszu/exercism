def prime(number):
    if number <= 0:
        raise ValueError('there is no zeroth prime')

    primes = []
    current = 2
    while len(primes) < number:
        if all(current % p > 0 for p in primes):
            primes.append(current)
        current += 1
    return primes[number-1]
