#Find the Missing Number:Find the missing number in an array of size n containing numbers from 1 to n
def find_missing(arr, n):
    for num in range(1, n + 1):
        found = False

        for x in arr:
            if x == num:
                found = True
                break

        if not found:
            return num

    return -1

arr = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter value of n: "))

print("Missing number is:", find_missing(arr, n))