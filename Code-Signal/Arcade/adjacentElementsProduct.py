def adjacentElementsProduct(inputArray):
    maximum = inputArray[0] * inputArray [1]
    for i in range(1, len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > maximum:
            maximum = inputArray[i] * inputArray[i+1]
    return maximum
