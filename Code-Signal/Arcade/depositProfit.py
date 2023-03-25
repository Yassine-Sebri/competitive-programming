def depositProfit(deposit, rate, threshold):
    output = 0
    while deposit < threshold:
        deposit *= 1 + rate / 100
        output += 1
    return output
