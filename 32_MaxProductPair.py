#Find Maximum Product Pair: Find two elements whose product is maximum.
def max_product_pair(arr):
    n = len(arr)
    max_product = arr[0] * arr[1]
    a = arr[0]
    b = arr[1]

    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]

            if product > max_product:
                max_product = product
                a = arr[i]
                b = arr[j]

    print("Maximum product pair:", a, b)


arr = list(map(int, input("Enter numbers: ").split()))
max_product_pair(arr)