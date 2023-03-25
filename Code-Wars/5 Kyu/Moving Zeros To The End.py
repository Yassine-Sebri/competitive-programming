"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements."""

def move_zeros(array):
    zeroes = []
    not_zeroes = []
    for element in array:
        if element == 0 and not(element is False):
            zeroes = zeroes + [0]
        else:
            not_zeroes = not_zeroes + [element]
    return not_zeroes + zeroes
