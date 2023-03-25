def sortByHeight(a):
    ordered = filter(lambda x: x!=-1, sorted(a))
    ordered = [i for i in ordered]
    i = 0
    for index, number in enumerate(a):
        if number != -1:
            a[index] = ordered[i]
            i += 1
    return a
