#Find the First Missing Positive: Find the smallest positive integer missing in the array.
def first_missing_positive(arr):
    n = len(arr)

    for num in range(1, n + 2):
        found = False

        for x in arr:
            if x == num:
                found = True
                break

        if not found:
            return num

    return -1


arr = list(map(int, input("Enter numbers: ").split()))
print("First missing positive:", first_missing_positive(arr))