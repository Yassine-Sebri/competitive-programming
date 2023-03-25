def alternatingSums(a):
    s1 = 0
    s2 = 0
    for index, number in enumerate(a):
        if index % 2:
            s2 += number
        else:
            s1 += number
    return [s1, s2]
