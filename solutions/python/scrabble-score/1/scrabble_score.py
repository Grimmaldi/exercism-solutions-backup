def score(word):
    total = 0
    letter_points = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
                     ('D', 'G'): 2,
                     ('B', 'C', 'M', 'P'): 3,
                     ('F', 'H', 'V', 'W', 'Y'): 4,
                     ('K',): 5,
                     ('J', 'X'): 8,
                     ('Q', 'Z'): 10}

    for letter in word.upper():
        total += next(value for key, value in letter_points.items() if letter in key)

    return total