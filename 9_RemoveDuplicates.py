#Remove Duplicates from Array: Remove duplicates from the array while maintaining order. 
def remove_duplicates(arr):
    result = []

    for num in arr:
        found = False

        for x in result:
            if x == num:
                found = True
                break

        if not found:
            result.append(num)

    return result

arr = list(map(int, input("Enter numbers: ").split()))
print("Array after removing duplicates:", remove_duplicates(arr))