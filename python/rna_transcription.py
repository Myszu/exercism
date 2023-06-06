def to_rna(dna_strand):
    dict = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    output = ''
    for letter in dna_strand:
        output = output + dict.get(letter, letter)
    return output
