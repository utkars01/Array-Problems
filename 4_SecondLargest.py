#Find the Second Largest Element
def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

arr = list(map(int, input("Enter numbers: ").split()))
print("Second largest element is:", second_largest(arr))