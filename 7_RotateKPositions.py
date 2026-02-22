#Rotate Array by k Positions: Rotate the array to the right by k positions
def rotate_right(arr, k):
    n = len(arr)

    for _ in range(k):
        last = arr[n - 1]

        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]

        arr[0] = last

    return arr

arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter value of k: "))

print("Array after right rotation:", rotate_right(arr, k))