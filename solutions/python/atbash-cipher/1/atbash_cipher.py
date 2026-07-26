import string


def encode(decoded_string):
    decoded_string = ''.join(char for char in (decoded_string.lower()) if char.isalnum())
    alphabet = list(string.ascii_lowercase)
    cipher = list(reversed(alphabet))
    result = ''
    for letter in enumerate(decoded_string):
        if (letter[0] + 1) % 5 == 0:
            if letter[1].isalpha() == True:
                result += cipher[alphabet.index(letter[1])] + ' '
            else:
                result += letter[1] + ' '
        elif letter[1].isdigit() == True:
            result += letter[1]
        else:
            result += cipher[alphabet.index(letter[1])]
    return result.strip()


def decode(encoded_string):
    alphabet = list(string.ascii_lowercase)
    cipher = list(reversed(alphabet))
    result = ''
    for letter in encoded_string:
            if letter != ' ':
                result += alphabet[cipher.index(letter)]
    return result.strip()