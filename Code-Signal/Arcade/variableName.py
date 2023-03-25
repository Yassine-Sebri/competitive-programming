def variableName(name):
    if name[0].isdigit():
        return False
    for letter in name:
        if not letter.isdigit() and not letter.isalpha() and letter != '_':
            return False
    return True
