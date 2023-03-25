def calculate_neighbors(matrix, i, j):
    output = 0
    try:
        if matrix[i - 1][j - 1] and i > 0 and j > 0:
            output += 1
    except:
        pass
    try:
        if matrix[i - 1][j] and i > 0:
            output += 1
    except:
        pass
    try:
        if matrix[i - 1][j + 1] and i > 0:
            output += 1
    except:
        pass
    try:
        if matrix[i][j - 1] and j > 0:
            output += 1
    except:
        pass
    try:
        if matrix[i][j + 1]:
            output += 1
    except:
        pass
    try:
        if matrix[i + 1][j - 1] and j > 0:
            output += 1
    except:
        pass
    try:
        if matrix[i + 1][j]:
            output += 1
    except:
        pass
    try:
        if matrix[i + 1][j + 1]:
            output += 1
    except:
        pass
    return output


def minesweeper(matrix):
    output = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])):
            line.append(calculate_neighbors(matrix, i, j))
        output.append(line)
    return output
