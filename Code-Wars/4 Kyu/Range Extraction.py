"""A format for expressing an ordered list of integers is to use a comma separated list of
either

    individual integers
    
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
    The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
    at least 3 numbers. For example ("12, 13, 15-17")

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the
range format."""

def solution(args):
    temp = []
    index = 0
    while index < len(args):
        counter = 0
        while index < len(args)-1 and args[index+1] - args[index] == 1:
            counter += 1
            index += 1
        if counter > 1:
            temp.append('-'.join([str(args[index - counter]),str(args[index])]))
        elif counter == 1:
            temp += [str(args[index - 1]), str(args[index])]
        else:
            temp.append(str(args[index]))
        index += 1
    return ','.join(temp)
