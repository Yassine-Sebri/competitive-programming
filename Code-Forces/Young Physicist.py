def main():
    n = int(input())
    prob = []
    for i in range(n):
        prob.append([int(number) for number in input().split()])
    var1, var2, var3 = 0, 0, 0
    for ligne in prob:
        var1 += ligne[0]
        var2 += ligne[1]
        var3 += ligne[2]
    if var1 or var2 or var3:
        print('NO')
    else:
        print('YES')


main()
