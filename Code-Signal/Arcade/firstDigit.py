def firstDigit(inputString):
    for letter in inputString:
        if letter.isdigit():
            return letter
