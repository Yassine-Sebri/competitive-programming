def main():
    ch = list(input())
    prev = [ch[0]]
    for i in ch[1:]:
        if prev and i == prev[-1]:
            prev.pop()
        else:
            prev.append(i)
    print("".join(prev))


main()
