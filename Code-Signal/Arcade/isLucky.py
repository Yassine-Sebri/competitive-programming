def isLucky(n):
    return sum([int(i) for i in str(n)[:len(str(n))//2]]) == sum([int(i) for i in str(n)[len(str(n))//2:]])
