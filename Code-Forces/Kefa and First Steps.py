def main():
    input()
    prob = [int(number) for number in input().split()]
    curr = 1
    maximum = 1
    for i in range(1, len(prob)):
        if prob[i-1] <= prob[i]:
            curr += 1
        else:
            maximum = max(maximum, curr)
            curr = 1
    maximum = max(maximum, curr)
    print(maximum)


main()
