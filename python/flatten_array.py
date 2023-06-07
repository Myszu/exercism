def flatten(iterable):
    output = []
    for unit in iterable:
        if isinstance(unit, int):
            output.append(unit)
        if isinstance(unit, list):
            output.extend(flatten(unit))
    return output
