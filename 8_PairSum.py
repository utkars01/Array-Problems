#Find Pair with Given Sum: Find a pair of elements that adds up to a target sum
def find_all_pairs(arr, target):
    found = False

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print("Pair found:", arr[i], arr[j])
                found = True

    if not found:
        print("No pair found")


arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

find_all_pairs(arr, target)