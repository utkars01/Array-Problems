#Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers
def longest_consecutive(arr):
    n = len(arr)
    longest = 0

    for i in range(n):
        current = arr[i]
        length = 1

        while True:
            found = False

            for j in range(n):
                if arr[j] == current + 1:
                    found = True
                    current += 1
                    length += 1
                    break

            if not found:
                break

        if length > longest:
            longest = length

    return longest


arr = list(map(int, input("Enter numbers: ").split()))
print("Longest consecutive length:", longest_consecutive(arr))