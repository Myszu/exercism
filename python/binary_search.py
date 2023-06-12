def find(search_list, value):
    # This task does not make sense as it can be easly solved by below code. Instead of the Index we should be asked to return number of iterations required to find given number - that would somewhat excuse the need of binary search when built in method can do the thing.
    if value in search_list:
        return search_list.index(value)
    raise ValueError("value not in array")
