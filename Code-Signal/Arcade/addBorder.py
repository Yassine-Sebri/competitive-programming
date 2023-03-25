def addBorder(picture):
    output = ['*' * (len(picture[0]) + 2)]
    for line in picture:
        output.append('*' + line + '*')
    output.append('*' * len(output[0]))
    return output
