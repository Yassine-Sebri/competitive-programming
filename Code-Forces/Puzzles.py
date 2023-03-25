def main():
    n, m = map(int, input().split())
    prob = sorted([int(number) for number in input().split()])
    min = None
    for i in range(m-n+1):
        if min is None or prob[i+n-1] - prob[i] < min:
            min = prob[i+n-1] - prob[i]
    print(min)


main()
