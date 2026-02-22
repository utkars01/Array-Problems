#Find All Subarrays
def print_all_subarrays(arr):
    n = len(arr)

    print("All subarrays are:")

    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()


arr = list(map(int, input("Enter numbers: ").split()))
print_all_subarrays(arr)