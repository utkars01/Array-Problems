#Find Peak Element: A peak element is greater than its neighbors. Find one such element.
def find_peaks(arr):
    n = len(arr)
    print("Peak elements are:")

    found = False

    for i in range(n):
        left_ok = (i == 0 or arr[i] >= arr[i - 1])
        right_ok = (i == n - 1 or arr[i] >= arr[i + 1])

        if left_ok and right_ok:
            print(arr[i], end=" ")
            found = True

    if not found:
        print("No peak found")


arr = list(map(int, input("Enter numbers: ").split()))
find_peaks(arr)