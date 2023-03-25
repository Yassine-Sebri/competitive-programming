from sys import stdin, stdout


def main():
    n, m = map(int, stdin.readline().split())
    output = 0
    while n <= m:
        n, m = n * 3, m * 2
        output += 1
    stdout.write(str(output))


main()
