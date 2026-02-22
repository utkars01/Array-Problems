# Find Equilibrium Index: Find an index such 
# that sum of elements on left = sum on right
def equilibrium_index(arr):
    n = len(arr)

    for i in range(n):
        left_sum = 0
        right_sum = 0

        for j in range(i):
            left_sum += arr[j]

        for j in range(i + 1, n):
            right_sum += arr[j]

        if left_sum == right_sum:
            return i

    return -1


arr = list(map(int, input("Enter numbers: ").split()))
print("Equilibrium index:", equilibrium_index(arr))