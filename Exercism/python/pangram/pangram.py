from string import ascii_lowercase

def is_pangram(sentence):
    d = dict.fromkeys(ascii_lowercase, False)

    for char in sentence:
        char = char.lower()
        d[char] = True
    
    return all(d.values())
