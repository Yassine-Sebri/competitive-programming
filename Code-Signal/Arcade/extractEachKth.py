def extractEachKth(inputArray, k):
    return [number for index, number in enumerate(inputArray) if index % k != k - 1]
