# TO-DO:
# 1. maxHeapify (X)
# 2. buildMaxHeap (X)
# 3. sort (X)
# 4. extractMax (X)
# 5. insert (X)

import math


class Heap:
    def __init__(self, arr):
        # buildMaxHeap
        self.size = len(arr)

        # Prefix with None to have a 1-indexed array
        self.arr = [None] + arr

        # maxHeapify all nodes upto n/2. Rest are leaves and are hence max-heaps already
        for i in range(math.floor(self.size / 2), 0, -1):
            self.arr = self.maxHeapify(self.arr, self.size, i)

    def maxHeapify(self, arr, size, index):
        # Initialize children
        left = 2 * index
        right = 2 * index + 1

        largest = index

        # Find the largest element between the parent, left and right
        if left <= size and arr[left] > arr[largest]:
            largest = left
        if right <= size and arr[right] > arr[largest]:
            largest = right

        # If parent isn't the largest, swap and recurse
        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            self.maxHeapify(arr, size, largest)

        return arr

    def sort(self):
        # Heap sort

        # Ans array contains the sorted elements. OG heap stays the same
        ans = self.arr
        size = self.size

        # For the entire array, swap 1st and last and then maxHeapify
        while size > 0:
            ans[size], ans[1] = ans[1], ans[size]
            size -= 1
            ans = self.maxHeapify(ans, size, 1)

        return ans[1:]

    def extractMax(self):
        # If the heap is empty, return None
        if self.size < 1:
            return None

        # The first element is the max
        ans = self.arr[1]

        # swap 1st and last elements
        self.arr[1], self.arr[self.size] = self.arr[self.size], self.arr[1]

        # Decrement the size
        self.size -= 1

        # Maintain heap property
        self.arr = self.maxHeapify(self.arr, self.size, 1)

        return ans

    def getHeap(self):
        # Returns current heap
        return self.arr[1 : self.size + 1]

    def add(self, val):
        self.arr = self.arr[: self.size + 1]  # In case we extracted some elements

        # Append new value
        self.arr.append(val)
        self.size += 1

        # Bubble up the new value by comparing to parent
        i = self.size
        p = math.floor(i / 2)

        while p > 0 and self.arr[i] > self.arr[p]:
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p
            p = math.floor(i / 2)

        return val
