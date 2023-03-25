def palindromeRearranging(inputString):
    letters = {}
    for letter in inputString:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    first = True
    output = True
    for letter in letters:
        if letters[letter] % 2 == 1:
            if first:
                first = False
            else:
                output = False
                break
    return output
