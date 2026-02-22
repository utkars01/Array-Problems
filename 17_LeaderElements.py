#Find the Leader Elements: An element is a leader if it is greater than all elements to its right
def find_leaders(arr):
    print("Leader elements are:")

    n = len(arr)

    for i in range(n):
        is_leader = True

        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                is_leader = False
                break

        if is_leader:
            print(arr[i])


arr = list(map(int, input("Enter numbers: ").split()))
find_leaders(arr)