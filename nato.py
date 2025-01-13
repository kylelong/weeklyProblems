def natoify(str):
    alphabet_mapping = {
    'a': 'Alfa', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta',
    'e': 'Echo', 'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel',
    'i': 'India', 'j': 'Juliett', 'k': 'Kilo', 'l': 'Lima',
    'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa',
    'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
    'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray',
    'y': 'Yankee', 'z': 'Zulu',
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three',
    '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
    '8': 'Eight', '9': 'Nine',
    '.': 'Stop', ',': 'Comma', '-': 'Hyphen (Dash)', 
    '/': 'Slant', '(': 'Brackets On', ')': 'Brackets Off',
    ':': 'Colon', ';': 'Semi-Colon', '!': 'Exclamation Mark',
    '?': 'Question Mark', "'": 'Apostrophe',
    '"': 'Quote', '"': 'Unquote', ' ': '(Space)'
}

    return ' '.join(list(map(lambda x: alphabet_mapping[x], list(str.lower()))))
assert natoify('hello world') == "Hotel Echo Lima Lima Oscar (Space) Whiskey Oscar Romeo Lima Delta"
assert natoify('3spooky5me') == "Three Sierra Papa Oscar Oscar Kilo Yankee Five Mike Echo"