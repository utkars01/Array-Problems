#Find Subarray with Given Sum.
def subarray_with_sum(arr, target):
    n = len(arr)

    for i in range(n):
        current_sum = 0

        for j in range(i, n):
            current_sum += arr[j]

            if current_sum == target:
                print("Subarray found from index", i, "to", j)
                return

    print("No subarray found")


arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

subarray_with_sum(arr, target)