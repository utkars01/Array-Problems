#Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements
def move_zeroes(arr):
    result = []
    zero_count = 0

    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)

    for _ in range(zero_count):
        result.append(0)

    return result


arr = list(map(int, input("Enter numbers: ").split()))
print("After moving zeroes:", move_zeroes(arr))