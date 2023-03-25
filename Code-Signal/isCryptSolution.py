def isCryptSolution(crypt, solution):
    mapping = {i[0]: i[1] for i in solution}
    word1 = "".join([mapping[letter] for letter in crypt[0]])
    word2 = "".join([mapping[letter] for letter in crypt[1]])
    word3 = "".join([mapping[letter] for letter in crypt[2]])
    if (word1[0] == '0' and len(word1) > 1) or (word2[0] == '0' and len(word1) > 1) or (word3[0] == '0' and len(word1) > 1):
        return False
    return int(word1) + int(word2) == int(word3)
