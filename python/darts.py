def score(x, y):
    x = x.real.__abs__()
    y = y.real.__abs__()
    if x**2 + y**2 - 1 <= 0:
        return 10
    if x**2 + y**2 - 25 <= 0:
        return 5
    if x**2 + y**2 - 100 > 0:
        return 0
    return 1
