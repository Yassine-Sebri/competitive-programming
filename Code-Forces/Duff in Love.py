def main():
    n = int(input())
    i = 2
    while n >= i ** 2:
        while n % i ** 2 == 0:
            n //= i
        i += 1
    print(n)


main()
