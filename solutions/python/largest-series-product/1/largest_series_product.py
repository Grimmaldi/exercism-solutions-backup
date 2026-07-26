def largest_product(num_string, series_length):
    if series_length == 0:
        return 1
    elif (len(num_string) < series_length) or (series_length < 0) or (num_string == ""):
        raise ValueError
    else:
        result, string_index = 0, 0
        while (string_index + series_length) < len(num_string) + 1:
            base = 1
            templist = list(map(int, list(num_string[string_index:(string_index + series_length)])))
            if 0 not in templist:
                for number in templist:
                    base *= number
                    if base > result:
                        result = base
            string_index += 1
        return result