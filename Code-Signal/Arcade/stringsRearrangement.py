from itertools import permutations

def diff_one_char(string1, string2):
    different = False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if not different:
                different = True
            else:
                return False
    return different

def stringsRearrangement(inputArray):
    for p in permutations(inputArray):
        maybe = True
        for i in range(1, len(p)):
            if not diff_one_char(p[i-1], p[i]):
                maybe = False
                break
        if maybe:
            return True
    return False
