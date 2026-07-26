def distance(strand1, strand2):
    dist, letter_compared = 0, 0

    if len(strand1.strip()) == len(strand2.strip()):
        for letter in strand1:
            if letter != strand2[letter_compared]:
                dist += 1
            else:
                pass
            letter_compared += 1
        return dist
    else:
        raise ValueError