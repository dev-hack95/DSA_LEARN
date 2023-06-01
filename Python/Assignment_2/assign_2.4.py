def func(arr, n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0 and (i == 0 or arr[i - 1] == 0) and (i == len(arr) - 1 or arr[i + 1] == 0):
            arr[i] = 1
            count += 1

    return count >= n

print(func([1, 0, 0, 0, 1], 1))