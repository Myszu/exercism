def translate(text):
    translation = []
    words = text.split()
    if len(words) > 1:
        for word in words:
            translation.append(translate(word))
        return ' '.join(translation)
    else:
        word = words[0]
        vowels = 'aeiou'
        con_clus = ['ch','squ','qu','thr','th','sch','rh']
        edge_cases = ['xr','yt']
        if word[0] in vowels:
            return word+'ay'
        else:
            for cluster in con_clus:
                if word.startswith(cluster):
                    return word[len(cluster):]+cluster+'ay'
            for case in edge_cases:
                if word.startswith(case):
                    return word+'ay'
            else:
                return word[1:]+word[0]+'ay'
