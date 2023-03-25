"""Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a 
positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n."""

def dig_pow(n, p):
    temp = [int(digit) ** (p+index) for index, digit in enumerate(str(n))]
    return sum(temp) // n if sum(temp) % n == 0 else -1 
