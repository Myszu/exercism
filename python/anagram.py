def find_anagrams(word, candidates):
    output = []
    sorted_word = ''.join(sorted(list(word.lower())))
    for candidate in candidates:
        if word.lower() == candidate.lower():           
            continue
        sorted_candidate = ''.join(sorted(list(candidate.lower())))
        if sorted_word == sorted_candidate:
            output.append(candidate)
    return output
