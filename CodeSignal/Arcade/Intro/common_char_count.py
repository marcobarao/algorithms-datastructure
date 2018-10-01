def commonCharacterCount(s1, s2):
    s1_set = set(s1)
    total = 0
    
    for char in s1_set:
        total += min(s2.count(char), s1.count(char))

    return total