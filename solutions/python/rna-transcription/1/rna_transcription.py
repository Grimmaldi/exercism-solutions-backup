def to_rna(dna):
    rna_translation = ''
    for character in dna:
        if character == 'G':
            rna_translation += 'C'
        elif character == 'C':
            rna_translation += 'G'
        elif character == 'T':
            rna_translation += 'A'
        elif character == 'A':
            rna_translation += 'U'
        else:
            return ''
    return rna_translation