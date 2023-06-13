def append(list1, list2):
    output = []
    for element in list1:
        output.append(element)
    for element in list2:
        output.append(element)
    return output


def concat(lists):
    return [element for unit in lists for element in unit]


def filter(function, list):
    return [unit for unit in list if function(unit)]


def length(list):
    return sum(1 for unit in list)


def map(function, list):
    return [function(unit) for unit in list]


def foldl(function, list, initial):
    for unit in list:
	    initial = function(initial, unit)
    return initial


def foldr(function, list, initial):
    for unit in list[::-1]:
	    initial = function(initial, unit)
    return initial


def reverse(list):
    return list[::-1]
