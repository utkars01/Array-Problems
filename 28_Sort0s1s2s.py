#Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s
def sort_012(arr):
    count0 = 0
    count1 = 0
    count2 = 0

    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    index = 0

    for _ in range(count0):
        arr[index] = 0
        index += 1

    for _ in range(count1):
        arr[index] = 1
        index += 1

    for _ in range(count2):
        arr[index] = 2
        index += 1

    return arr


arr = list(map(int, input("Enter 0s,1s,2s: ").split()))
print("Sorted array:", sort_012(arr))