def transpose(lines):
    splited = lines.split('\n')
    longest = max(map(len, splited))
    lines = map(lambda line: line + '\0'* (longest - len(line)), splited)
    return '\n'.join(map(lambda line: ''.join(line).rstrip('\0'), zip(*lines))).replace('\0',' ')
