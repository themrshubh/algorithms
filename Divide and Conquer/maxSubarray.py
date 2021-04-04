# Maximum subarray problem
# Given input of an array of numbers, determine the contiguous subarray whose values have the greatest sum.
# Ex: [-1,2,3,-5,6,7] => ans = 13

import math


def findMaximumSum(start, end, arr):
    if start == end:
        # array has only one element
        return arr[start]

    # Find the mid index
    mid = math.floor((start + end) / 2)

    # Maximum sum subarray on the right and left of mid
    leftMax = findMaximumSum(start, mid, arr)
    rightMax = findMaximumSum(mid + 1, end, arr)

    # Maximum sum subarray that crosses the mid element
    crossMax = findCrossMaximum(start, end, mid, arr)

    return max(leftMax, rightMax, crossMax)


def findCrossMaximum(start, end, mid, arr):
    # Sum of numbers to the left of mid
    leftSum = -math.inf
    total = 0
    left = mid

    while left >= start:
        total += arr[left]
        leftSum = max(leftSum, total)
        left -= 1

    # Sum of numbers to the right of mid
    rightSum = -math.inf
    total = 0
    right = mid + 1

    while right <= end:
        total += arr[right]
        rightSum = max(rightSum, total)
        right += 1

    # Max sum of numbers that pass through mid
    return leftSum + rightSum


arr = [-1, 2, 3, -5, 6, 7]
ans = findMaximumSum(0, len(arr) - 1, arr)
print(ans)
