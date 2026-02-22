#Find the Sum of Elements
def find_sum(arr):
    total = 0
    for num in arr:
        total = total + num
    return total

arr = list(map(int, input("Enter numbers: ").split()))
print("Sum of elements is:", find_sum(arr))