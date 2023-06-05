def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    distance = 0
    for i, letter in enumerate(strand_a):
        if letter != strand_b[i]:
            distance += 1
    return distance
