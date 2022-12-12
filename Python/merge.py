import numpy as np
import time

start_time = 0
end_time = 0


def num_gen(x):
    arr = np.random.randint(0, x, x)
    return arr


def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):

    if l < r:

        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


x = int(input("Enter How many number to generate \n"))
arr = num_gen(x)
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time() - start_time
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTime: ", end_time)
