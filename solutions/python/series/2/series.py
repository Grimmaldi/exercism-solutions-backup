def slices(numstring, slicelen):
    result = []
    if (slicelen > len(numstring)) or (slicelen == 0):
        raise ValueError
    else:
        for character in enumerate(numstring):
            if (character[0] + slicelen) > len(numstring):
                break
            else:
                result.append(list(map(int, numstring[(character[0]):(character[0]+slicelen)])))
        return result