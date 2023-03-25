def arrayMaxConsecutiveSum(inputArray, k):
    max = 0
    for index, number in enumerate(inputArray):
        if index < k:
            max += number
            if index == k - 1:
                current = max
        else:
            current = current + number - inputArray[index - k]
            if max < current:
                max = current
    return max
