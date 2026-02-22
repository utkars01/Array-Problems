# Find Intersection of Two Arrays: Find the common elements between two arrays.
def intersection(arr1, arr2):
    result = []

    for num in arr1:
        found_in_arr2 = False

        for x in arr2:
            if num == x:
                found_in_arr2 = True
                break

        if found_in_arr2:
            already_added = False

            for y in result:
                if y == num:
                    already_added = True
                    break

            if not already_added:
                result.append(num)

    return result

arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

print("Intersection:", intersection(arr1, arr2))