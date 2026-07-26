def sum_of_multiples(end_point, list_of_multiples):
    result = []
    test_range = list(range(end_point))
    for number in list_of_multiples:
        if number != 0:
            for possible_multiple in test_range:
                if possible_multiple % number == 0:
                    result.append(possible_multiple)
        else:
            result.append(0)
            continue
    return sum(set(result))