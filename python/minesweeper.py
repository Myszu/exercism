def annotate(minefield):
    output = []
    if len(minefield)==0 or len(minefield[0])==0: return minefield
    if not all([True if len(row) == len(minefield[0]) else False for row in minefield]):
        raise ValueError("The board is invalid with current input.")

    for r in range(len(minefield)):
        row = ''
        for i in range(len(minefield[r])):
            if not minefield[r][i] in (' ', '', '*'):
                raise ValueError("The board is invalid with current input.")
            if minefield[r][i]!=' ':
                row = f'{row}{minefield[r][i]}'
                continue
            count = sum(
                [
                    check(minefield, r-1, i-1),
                    check(minefield, r-1, i),
                    check(minefield, r-1, i+1),
                    check(minefield, r, i-1),
                    check(minefield, r, i+1),
                    check(minefield, r+1, i-1),
                    check(minefield, r+1, i),
                    check(minefield, r+1, i+1),
                ]
            )
            if count == 0: count = ' '
            row = f'{row}{count}'
        output.append(row)
    return output


def check(minefield, r, i):
    if r == -1 or i == -1: return 0
    try:
        return 1 if minefield[r][i]=='*' else 0
    except:
        return 0