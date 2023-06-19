SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        if list_one == list_two:
            return EQUAL
        return UNEQUAL
    if len(list_one) > len(list_two):
        longer, shorter = list_one, list_two
        options = [SUPERLIST, UNEQUAL]
    else:
        shorter, longer = list_one, list_two
        options = [SUBLIST, UNEQUAL]
    for i in range(0, len(longer)):
        if shorter == longer[i:i+len(shorter)]:
            return options[0]
    return options[1]
