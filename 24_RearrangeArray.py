#Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest. 
def rearrange_alternate(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    result = []
    left = 0
    right = n - 1

    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])

        left += 1
        right -= 1

    return result


arr = list(map(int, input("Enter numbers: ").split()))
print("Rearranged array:", rearrange_alternate(arr))