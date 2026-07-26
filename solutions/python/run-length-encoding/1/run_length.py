def encode(uncompressed_string):
    source_string = uncompressed_string.strip()
    result, temp_string, temp_count, string_position = [], '', 1, 1
    for letter in source_string:
        if string_position + 1 > len(source_string):
            temp_string = str(temp_count) + letter
            if len(temp_string) == 2 and temp_string[0] == '1':
                result.append(letter)
            else:
                result.append(temp_string)
        elif letter != source_string[string_position]:
            temp_string = str(temp_count) + letter
            if len(temp_string) == 2 and temp_string[0] == '1':
                result.append(letter)
                temp_count = 1
                string_position += 1
            else:
                result.append(temp_string)
                temp_count = 1
                string_position += 1
        else:
            temp_count += 1
            temp_string = str(temp_count) + source_string[string_position]
            string_position += 1

    return ''.join(result)


def decode(compressed_string):
    source_string = compressed_string.strip()
    result, temp_num, temp_count, string_position = [], '', 1, 1
    for letter in source_string:
        if letter.isdigit() is True:
            temp_num += letter
        elif temp_num != '':
            result.append(str(int(temp_num) * letter))
            temp_num = ''
        else:
            result.append(letter)
    return ''.join(result)