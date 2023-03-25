def almostIncreasingSequence(sequence):
    first = True
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            if first:
                first = False
                if i > 0 and sequence[i-1] >= sequence[i+1]:
                    if i < len(sequence) - 2 and sequence[i] >= sequence[i+2]:
                        return False
            else:
                return False
    return True
