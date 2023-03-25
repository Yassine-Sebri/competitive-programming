def reverseInParentheses(inputString):
    if inputString.count('(') == 0:
        return inputString
    else:
        i = 0
        start = None
        end = None
        while i < len(inputString):
            if inputString[i] == '(':
                start = i
            if inputString[i] == ')':
                end = i
            if start is not None and end is not None:
                a = inputString[:start]
                b = inputString[end - 1:start:-1]
                c = inputString[end + 1:] if len(inputString) - 1 > end else ''
                inputString = a + b + c
                start = None
                end = None
                i -= 1
            i += 1
        return reverseInParentheses(inputString)
