#
# Skeleton file for the Python "Bob" exercise.
#


def hey(you_say):
    if str(you_say).isupper() is True:
        return 'Whoa, chill out!'
    elif  str(you_say).strip().endswith('?'):
        return 'Sure.'
    elif str(you_say).strip() == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'