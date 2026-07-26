def say(raw_number):
    if raw_number == 0:
        return 'zero'
    elif raw_number < 0 or raw_number > 999999999999:
        raise AttributeError('Must be a positive integer less than 1000000000000.')
    else:
        text_version = ''
        number = str(int(raw_number)).rjust(12, '0')
        source = [[number[:3]], [number[3:6]], [number[6:9]], [number[9:]]]
        number_group = [' billion ', ' million ', ' thousand ', '']
        for block in enumerate(source):
            if block[1] == ['000']:
                continue
            elif block[0] == 0 and number[3:10] == '0000000' and number[3:] != '000000000':
                text_version += hundreds(block[1][0]) + number_group[block[0]] + 'and '
            elif block[0] == 1 and number[6:10] == '0000' and number[6:] != '000000':
                text_version += hundreds(block[1][0]) + number_group[block[0]] + 'and '
            elif block[0] == 2 and number[9:10] == '0' and number[9:] != '000':
                text_version += hundreds(block[1][0]) + number_group[block[0]] + 'and '
            else:
                text_version += hundreds(block[1][0]) + number_group[block[0]]
        return text_version.strip()


def hundreds(number):
    test_number = list(number)
    text_version = ''
    ones = {'1': 'one', '2': 'two', '3': 'three', '4': 'four',
            '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    tens = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
            '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
    one_tens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
                '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
                '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    for numeral in enumerate(test_number):
                if numeral[0] == 0:
                    if numeral[1] != '0':
                        text_version += ones[numeral[1]] + ' hundred'
                        if number[1:] != '00':
                            text_version += ' and '
                elif numeral[0] == 1:
                    if numeral[1] == '1':
                        text_version += one_tens[number[1:]]
                        break
                    elif numeral[1] != '0':
                        text_version += tens[numeral[1]]
                else:
                    if numeral[1] != '0':
                        if test_number[1] != '0':
                            text_version += '-'
                        text_version += ones[numeral[1]]

    return text_version.strip()