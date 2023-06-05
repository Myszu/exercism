def is_pangram(sentence: str):
    pangram = 'abcdefghijklmnopqrstuvwxyz'
    output = ''.join(sorted(list(set(sentence.lower().replace(' ', ''))))).strip()
    if output.find(pangram) >= 0:
        return True
    return False
