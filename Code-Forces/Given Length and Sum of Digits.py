def main():
    m, s = map(int, input().split())
    s1 = s
    if s == 0 and m == 1:
        print(0, 0)
    elif s < 1 or s > 9*m:
        print('-1 -1')
    else:
        probmax = [0]*m
        for i in range(m-1):
            if s1 > 9:
                probmax[i] = 9
                s1 -= 9
        probmax[-1] = s - sum(probmax)
        probmax.sort(reverse=True)

        probmin = [0]*m
        if s < 9*(m-1) + 2:
            probmin[0] = 1
            for i in range(m-1):
                if s <= 9*(m-i-2):
                    probmin[i+1] = 0
                elif s <= 9*(m-i-1):
                    probmin[i+1] = s - 1 - 9*(m-i-2)
                else:
                    probmin[i + 1] = 9
        else:
            probmin[0] = s - 9*(m-1)
            for i in range(m-1):
                probmin[i+1] = 9
        print("".join([str(number) for number in probmin]), "".join([str(number) for number in probmax]))


main()
