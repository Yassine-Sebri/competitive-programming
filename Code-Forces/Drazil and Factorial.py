def main():
    length = int(input())
    n = [int(digit) for digit in input() if digit != '0' and digit != '1']
    factorial = {2: [2], 3: [3], 4: [2, 2, 3], 5: [5], 6: [5, 3], 7: [7], 8: [7, 2, 2, 2], 9: [7, 3, 3, 2]}
    result = []
    for number in n:
        result += factorial[number]
    result = sorted(result, reverse=True)
    result = map(str, result)
    print(''.join(result))


main()
