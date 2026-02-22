#Rotate Array to the Left by k Positions 
def rotate_left(arr, k):
    n = len(arr)

    for _ in range(k):
        first = arr[0]

        for i in range(n - 1):
            arr[i] = arr[i + 1]

        arr[n - 1] = first

    return arr


arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter value of k: "))

print("Array after left rotation:", rotate_left(arr, k))