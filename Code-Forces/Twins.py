def main():
    n = input()
    prob = sorted([int(number) for number in input().split()], reverse=True)
    index = 1
    while sum(prob[:index]) <= sum(prob[index:]):
        index += 1
    print(len(prob[:index]))


main()
