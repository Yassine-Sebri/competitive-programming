def commonCharacterCount(s1, s2):
    letters1 ={}
    letters2 ={}
    for letter in (s1):
        if letter not in letters1:
            letters1[letter] = 1
        else:
            letters1[letter] += 1
    for letter in (s2):
        if letter not in letters2:
            letters2[letter] = 1
        else:
            letters2[letter] += 1
    output = 0
    for letter in letters1:
        if letter in letters2:
            output += min(letters1[letter], letters2[letter])
    return output
