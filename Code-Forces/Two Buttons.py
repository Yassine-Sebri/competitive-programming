def main():
    n, m = map(int, input().split())
    count = 0
    while m != n:
        if n > m:
            count += n - m
            break
        else:
            if m % 2:
                m += 1
            else:
                m /= 2
            count += 1
    print(int(count))


main()
