def func(arr):
    arr.sort()
    n = len(arr)
    product_1 = arr[n - 1] * arr[n - 2] * arr[n - 3]
    
    if arr[0] < 0 and arr[1] < 0 and arr[n - 1] > 0:
        product = arr[0] * arr[1] * arr[n - 1]
        product_1 = max(product_1, product)
        
    return product_1


print(func([1, 2, 3]))
 

