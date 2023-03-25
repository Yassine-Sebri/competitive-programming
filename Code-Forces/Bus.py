def main():
    a, b, f, k = map(int, input().split())
    if b < f or b < a - f:
        print(-1)
    elif k >= 2 and b < 2 * (a - f):
        print(-1)
    elif k > 2 and b < 2 * f:
        print(-1)
    else:
        refuel, fuel = 0, b
        for i in range(k - 1):
            if i % 2:
                if fuel < f + a:
                    refuel += 1
                    fuel = b - f
                else:
                    fuel = fuel - a
            else:
                if fuel < 2 * a - f:
                    refuel += 1
                    fuel = b - (a - f)
                else:
                    fuel = fuel - a
        if fuel < a:
            refuel += 1
        print(refuel)


main()
