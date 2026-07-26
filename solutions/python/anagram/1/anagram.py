def detect_anagrams(word, candidates):
    """Returns a list of any words in the candidates argument that are anagrams
    of the word entered into the word argument."""

    anagrams = []
    word_test = sorted(list(word.lower()))

    if type(candidates) != list:
        candidates = candidates.split()

    for item in candidates:
        if len(item) != len(word) or word.lower() == item.lower():
            continue
        elif sorted(list(item.lower())) == word_test:
            anagrams.append(item)

    return anagrams