def is_paired(input_string):
    open = []
    for sign in input_string:
        if sign in ['[', '{', '(']:
            open.append(sign)
            continue
        if sign in [']', '}', ')'] and not open:
            return False
        if (sign == ']' and open[-1] == '[') or (sign == '}' and open[-1] == '{') or (sign == ')' and open[-1] == '('):
            open.pop(-1)
            continue
        if (sign == ']' and open[-1] != '[') or (sign == '}' and open[-1] != '{') or (sign == ')' and open[-1] != '('):
            return False
    if not open:
        return True
    return False
