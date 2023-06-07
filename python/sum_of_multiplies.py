def sum_of_multiples(limit, multiples):
    multis = []
    for multiple in multiples:
        for i in range(1, limit):
            output = multiple * i
            if output >= limit:
                break
            multis.append(output)
    multis = list(set(multis))
    return sum(multis)
