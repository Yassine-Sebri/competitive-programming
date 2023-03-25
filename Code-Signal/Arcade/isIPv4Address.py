def isIPv4Address(inputString):
    numbers = inputString.split('.')
    if len(numbers) != 4:
        return False
    for number in numbers:
        if not number.isdigit() or int(number) < 0 or int(number) > 255:
            return False
    return True
