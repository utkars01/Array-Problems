#. Product of Array Except Self Given an array,
# return a new array where each element is the product of all elements except itself. 
# Do not use division. Input: [1,2,3,4] Output: [24,12,8,6]
def product_except_self(arr):
    n = len(arr)
    result = []

    for i in range(n):
        product = 1

        for j in range(n):
            if i != j:
                product *= arr[j]

        result.append(product)

    return result


arr = list(map(int, input("Enter numbers: ").split()))
print("Product array:", product_except_self(arr))