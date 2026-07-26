class Cipher(object):

    import string

    alph = str(string.ascii_lowercase + string.ascii_lowercase)

    def __init__(self, key=''):
        self.key = str(key)

        if self.key == '':
            self.key = self.random_key()
        elif self.key.isalpha() is False or self.key.islower() is False:
            raise ValueError('The provided key must be lowercase, and have neither \
                              numerical nor special characters.')

    def encode(self, string_to_be_encoded):
        string_to_be_encoded = "".join(x for x in string_to_be_encoded.lower() if x.isalpha())
        encoded_string = ''
        temp_key = self.key

        while len(string_to_be_encoded) > len(temp_key):
            temp_key += temp_key

        delimited_key = temp_key[:len(string_to_be_encoded)]

        for x, y in zip(string_to_be_encoded, delimited_key):
            encoded_string_position = self.alph.find(x)
            key_position = self.alph.find(y)
            encoded_string += self.alph[encoded_string_position + key_position]

        return encoded_string

    def decode(self, encoded_string):
        decoded_string = ''
        encoded_string = ''.join(x for x in encoded_string if x.isalpha() and x is not ' ')
        temp_key = self.key

        while len(encoded_string) > len(temp_key):
            temp_key += temp_key

        delimited_key = temp_key[:len(encoded_string)]
        grouping = zip(encoded_string, delimited_key)

        for x, y in grouping:
            encoded_string_position = self.alph.rfind(x)
            key_position = self.alph.find(y)
            decoded_string += self.alph[encoded_string_position - key_position]

        return decoded_string

    def random_key(self):
        import random
        randkey = "".join(random.choice(self.alph) for x in range(100))
        return randkey


class Caesar(Cipher):

    def __init__(self):
        self.key = 'd'