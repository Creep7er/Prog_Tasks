array = [22, 32, 64, 12, 435, 86, 100, 2, 43]

left = 0
right = len(array) - 1

while left <= right:
    for i in range(left, right, +1):
        print(array)
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    right -= 1

    for i in range(right, left, -1):

        if array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
    left += 1

print(array)
