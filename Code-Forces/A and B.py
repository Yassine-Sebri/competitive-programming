def main():
    t = int(input())
    prob = []
    for i in range(t):
        prob.append([int(number) for number in input().split()])
    for ligne in prob:
        i = 0
        a, b = min(ligne[0], ligne[1]), max(ligne[0], ligne[1])
        while a != b:
            i += 1
            if b - a >= i:
                a += i
            else:
                b += i
        print(i)


main()
