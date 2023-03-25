def allLongestStrings(inputArray):
    max = None
    for string in inputArray:
        if max is None or len(string) > max:
            output = [string]
            max = len(string)
        elif len(string) == max:
            output.append(string)
    return output
