def distance(strand1, strand2):
    dist = 0
    if len(strand1.strip()) != len(strand2.strip()):
        raise ValueError
    else:
        zipped = zip(strand1,strand2)
        for item in zipped:
            if item[0] != item[1]:
                dist += 1
        return dist