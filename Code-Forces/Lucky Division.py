from sys import stdin, stdout


def main():
    n = int(input())
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 474, 777]
    lucky = False
    index = 0
    while not lucky and index < 14:
        lucky = (n % lucky_numbers[index]) == 0
        index += 1
    if lucky:
        print('YES')
    else:
        print('NO')


main()
