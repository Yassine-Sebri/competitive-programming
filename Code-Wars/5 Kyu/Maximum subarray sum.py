"""The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list 
of integers"""

def max_sequence(arr):
  maximum = 0
  current_max = 0
  for number in arr:
    if -number > maximum:
        maximum = 0
    else:
      maximum += number
    if maximum > current_max:
      current_max = maximum
  return current_max
