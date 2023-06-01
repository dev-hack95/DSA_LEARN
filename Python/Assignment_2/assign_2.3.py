def func(arr):
    len = 0
    for num in arr:
        count_num = 0
        count_num_1 = 0
        for n in arr:
            if n == num:
                count_num += 1
            elif n == num + 1:
                count_num_1 += 1
        if count_num_1 > 0:
            length = count_num + count_num_1
            len = max(len, length)

    return len

ans = func([1, 3, 2, 2, 5, 2, 3, 7])
print(ans)  
