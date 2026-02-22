#Count Frequency of Elements
def count_frequency(arr, key):
    count = 0

    for num in arr:
        if num == key:
            count += 1

    return count


arr = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter number to count: "))

result = count_frequency(arr, key)

print(key, "appears", result, "times")