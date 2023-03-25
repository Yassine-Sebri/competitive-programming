def boxBlur(image):
    height = len(image)
    width = len(image[0])
    output = []
    for i in range(1, height-1):
        line = []
        for j in range(1, width-1):
            line.append(int((image[i][j] + image[i][j+1] + image[i][j-1] + image[i+1][j] + image[i+1][j+1] + image[i+1][j-1] + image[i-1][j] + image[i-1][j+1] + image[i-1][j-1]) / 9))
        output.append(line)
    return output
