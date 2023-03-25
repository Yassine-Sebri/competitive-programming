def main():
    q=int(input())
    prob=[]
    for i in range(q):
        prob.append([int(number) for number in input().split()])
    for ligne in prob:
        y = ligne[3] // ligne[2]
        if y >= ligne[0]:
            if ligne[2] * ligne[0] + ligne[1] >= ligne[3]:
                print('YES')
            else:
                print('NO')
        else:
            if ligne[2] * y + ligne[1] >= ligne[3]:
                print('YES')
            else:
                print('NO')

main()
