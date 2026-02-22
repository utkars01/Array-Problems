#Find Maximum Difference (j > i)
def max_difference(arr):
    n = len(arr)
    max_diff = arr[1] - arr[0]

    for i in range(n):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]

            if diff > max_diff:
                max_diff = diff

    return max_diff


arr = list(map(int, input("Enter numbers: ").split()))
print("Maximum difference:", max_difference(arr))