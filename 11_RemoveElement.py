# Remove given Element from Array
def remove_element(arr, key):
    result = []

    for num in arr:
        if num != key:
            result.append(num)

    return result

arr = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter element to remove: "))

print("Array after removal:", remove_element(arr, key))