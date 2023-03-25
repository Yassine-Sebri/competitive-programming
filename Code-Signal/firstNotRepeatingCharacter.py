def firstNotRepeatingCharacter(s):
    initial = set()
    repetition = set()
    res = []
    for i in s:
        if i not in initial:
            initial.add(i)
            res.append(i)
        else:
            repetition.add(i)
    for i in res:
        if i not in repetition:
            return i
    return '_'
        
