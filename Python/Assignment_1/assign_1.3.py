"""
<aside>
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2

</aside>
"""

def func(target, arr):
    left = 0
    right = len(arr) - 1              

    while left <= right:
        mid = left + (right - left) // 2   # 1, 3, 5, 6

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left, arr

        
arr = [1,3,5,6]
ans = func(5, arr)

print(ans)

arr = [4, 2, 6, 7, 8]
ans_1 = func(5, arr)
print(ans_1)
