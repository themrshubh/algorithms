# Insertion sort
# Time complexity = O(n^2)
# Space complexity =

# Somewhat like sorting playing cards in hand

arr = [5, 2, 4, 6, 1, 7]

# Repeat from ind = 1 till the end
for i in range(1, len(arr)):
    # Current key
    key = arr[i]
    j = i - 1

    # Move everything more than the key, up the array
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    # Finally, set the key at it's position
    arr[j + 1] = key

print("Sorted array = ", arr)
