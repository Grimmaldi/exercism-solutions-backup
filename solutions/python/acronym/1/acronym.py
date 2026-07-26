import re


def abbreviate(source_text):
    regex = re.compile(r'^[A-Za-z]|(?<=-)[A-Za-z]|\s[A-Za-z]|(?<=[a-z])[A-Z]')
    return ''.join(re.findall(regex, source_text)).upper().replace(' ','')