def main():
    n = input()
    prob = [int(digit) for digit in n][::-1]
    res = []
    for i in range(max(prob)):
        num = 0
        for index, number in enumerate(prob):
            if number >= i+1:
                num += 10 ** index
        res.append(num)
    print(len(res))
    print(' '.join([str(number) for number in res]))


main()
