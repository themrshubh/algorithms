# Given an array; return sort it in increasing/ decreasing order
# Merge sort algorithm
# Time complexity = O(nlogn)

import math


def mergeSort(arr):
    # Array of length 1 or 0
    if len(arr) < 2:
        return arr

    # Indices in the array
    start = 0
    end = len(arr) - 1
    mid = math.floor((start + end) / 2)

    # Divide
    a = mergeSort(arr[: mid + 1])
    b = mergeSort(arr[mid + 1 :])

    # Conquer
    return merge(a, b)


def merge(arr1, arr2):
    p1, p2 = 0, 0
    ans = []

    # While neither pointer has reached the end
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            ans.append(arr1[p1])
            p1 += 1
        else:
            ans.append(arr2[p2])
            p2 += 1

    # In case one pointer reaches the end, copy all values from the other array
    while p1 < len(arr1):
        ans.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        ans.append(arr2[p2])
        p2 += 1

    return ans


# Input array
arr = [8, 7, 9, 4, 3, 9, 4, 2, 1, 1]

# Output
print(mergeSort(arr))
