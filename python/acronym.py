import re

def abbreviate(words):
    output = ''
    words = re.sub('[-_!@#$%^&*()]', ' ', words).split()
    for word in words:
        output += word.upper()[0]
    return output
