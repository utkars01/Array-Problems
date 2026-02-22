#Find Union of Two Arrays
def union_array(arr1, arr2):
    result = []

    for num in arr1:
        present = False

        for x in result:
            if x == num:
                present = True
                break

        if not present:
            result.append(num)

    for num in arr2:
        present = False

        for x in result:
            if x == num:
                present = True
                break

        if not present:
            result.append(num)

    return result

arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

print("Union:", union_array(arr1, arr2))