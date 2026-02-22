#Find the Kth Smallest Element
def kth_smallest(arr, k):
    n = len(arr)

    # bubble sort (ascending)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr[k - 1]


arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter value of k: "))

print("Kth smallest element is:", kth_smallest(arr, k))