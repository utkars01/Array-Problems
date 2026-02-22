#Maximum Sum Subarray (Kadane's Algorithm)
def max_subarray_sum(arr):
    n = len(arr)
    max_sum = arr[0]

    for i in range(n):
        current_sum = 0

        for j in range(i, n):
            current_sum += arr[j]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


arr = list(map(int, input("Enter numbers: ").split()))
print("Maximum subarray sum is:", max_subarray_sum(arr))