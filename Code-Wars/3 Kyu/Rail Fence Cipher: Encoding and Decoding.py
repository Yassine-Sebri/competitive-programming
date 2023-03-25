"""Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a
string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and
down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until
you reach the end of the string. Each "rail" is then read left to right to derive the encoded string."""

def encode_rail_fence_cipher(string, n):
    result = [[] for i in range(n)]
    for index, char in enumerate(string):
        index = index % (2 * (n-1))
        if index > n - 1:
            index = 2 * (n-1) - index
        result[index].append(char)
    return ''.join(''.join(rail) for rail in result)
    
def decode_rail_fence_cipher(string, n):
    print(n)
    if n == 2:
        return ''.join([char[i]+char[i+len(string)//2] for i in range(len(string) // 2)])
    result = [[] for i in range(n)]
    top = (len(string)-1) // (2 * (n-1)) + 1
    remain = (len(string)-1) % (2 * (n-1))
    result[0] = list(string[:top])
    string = string[top:]
    for i in range(n-2):
        if 2 * (n-1) - (i+1) <= remain:
            result[i+1]=list(string[:(top-1)*2 + 2])
            string = string[((top-1)*2 + 2):]
        elif (i+1) <= remain:
            result[i+1]=list(string[:(top-1)*2 + 1])
            string = string[((top-1)*2 + 1):]
        else:
            result[i+1]=list(string[:(top-1)*2])
            string = string[((top-1)*2):]
        result[-1] = list(string)
    print(result)
    string, i, k = '', 0, 1
    while result[i] != []:
        string += result[i].pop(0)
        if i == n - 1:
            k = -1
        elif i == 0:
            k = 1
        i += k
    print(string)
    return string
