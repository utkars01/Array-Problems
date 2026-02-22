#Find the Maximum & Minimum Element
def find_max_min(arr):
    maximum = arr[0]
    minimum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum

arr = list(map(int, input("Enter numbers: ").split()))
max, min = find_max_min(arr)
print("Maximum element is:", max)
print("Minimum element is:", min)