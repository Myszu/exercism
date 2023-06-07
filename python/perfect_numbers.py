def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    output = []
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1, number):
        if number%i == 0:
            output.append(i)
    summary = sum(output)
    if summary == number:
        return 'perfect'
    if summary > number:
        return 'abundant'
    return 'deficient'
