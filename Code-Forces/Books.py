def main():
    n, t = map(int, input().split())
    books = [int(number) for number in input().split()]
    maximum = 0
    for i in range(n):
        pointer1 = i
        if pointer1 > 0:
            time = time - books[pointer1 - 1]
        else:
            pointer2, time = 0, 0
        while pointer2 < n and (time + books[pointer2]) <= t:
            time += books[pointer2]
            pointer2 += 1
        if pointer2 - pointer1 > maximum:
            maximum = pointer2 - pointer1
    print(maximum)


main()
