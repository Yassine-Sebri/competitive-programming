def matrixElementsSum(matrix):
    rooms = len(matrix[0])
    haunted = [1 for i in range(rooms)]
    sum = 0
    for floor in matrix:
        for index in range(rooms):
            if haunted[index]:
                if floor[index]:
                    sum += floor[index]
                else:
                    haunted[index] = 0
    return sum
