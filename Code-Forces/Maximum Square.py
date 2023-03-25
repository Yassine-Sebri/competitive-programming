def main():
    t = int(input())
    prob = []
    for i in range(t):
        input()
        prob.append(sorted([int(number) for number in input().split()]))
    for line in prob:
        max = 1
        for index, number in enumerate(line):
            if max < number <= len(line) - index:
                max = number
            elif max < len(line) - index <= number:
                max = len(line) - index
                break
            elif len(line) - index < number:
                break
        print(max)


if __name__ == '__main__':
    main()