from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    prob = [''] * (n)
    for i in range(n-1):
        if i % 2:
            prob[i] = 'I love that'
        else:
            prob[i] = 'I hate that'
    if n % 2:
        prob[-1] = 'I hate it'
    else:
        prob[-1] = 'I love it'
    stdout.write(' '.join(prob))


main()
