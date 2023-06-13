def proteins(strand):
    output = []
    for i in range(0, len(strand)-1, 3):
        protein = recognize(strand[i:i+3])
        if protein:
            output.append(protein)
        else:
            break
    return output
        
        
def recognize(strand):
    if strand in ['AUG']:
        return 'Methionine'
    if strand in ['UUU', 'UUC']:
        return 'Phenylalanine'
    if strand in ['UUA', 'UUG']:
        return 'Leucine'
    if strand in ['UCU', 'UCC', 'UCA', 'UCG']:
        return 'Serine'
    if strand in ['UAU', 'UAC']:
        return 'Tyrosine'
    if strand in ['UGU', 'UGC']:
        return 'Cysteine'
    if strand in ['UGG']:
        return 'Tryptophan'
    if strand in ['UAA', 'UAG', 'UGA']:
        return ''
