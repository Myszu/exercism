import re
def count_words(sentence):
    words = re.findall(r"[a-z\d]+'?[a-z\d]+|\d+|[a-z]", sentence.lower())
    return {word: words.count(word) for word in words}
