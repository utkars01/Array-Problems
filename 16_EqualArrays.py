#Check if Two Arrays Are Equal: if two arrays contain the same elements
def arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True


arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

if arrays_equal(arr1, arr2):
    print("Arrays are equal")
else:
    print("Arrays are NOT equal")