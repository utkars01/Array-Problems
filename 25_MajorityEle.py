#Find Majority Element:Find the element that appears more than n/2 times.
def majority_element(arr):
    n = len(arr)

    for i in range(n):
        count = 0

        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        if count > n // 2:
            return arr[i]

    return -1


arr = list(map(int, input("Enter numbers: ").split()))
result = majority_element(arr)

if result == -1:
    print("No majority element")
else:
    print("Majority element is:", result)