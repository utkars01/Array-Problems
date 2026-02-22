# Find Duplicates in an Array
def find_duplicates(arr):
    visited = [False] * len(arr)

    print("Duplicate elements are:")

    for i in range(len(arr)):
        if visited[i]:
            continue

        count = 1

        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
                visited[j] = True

        if count > 1:
            print(arr[i])

arr = list(map(int, input("Enter numbers: ").split()))
find_duplicates(arr)