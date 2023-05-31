"""
<aside>
💡 Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

</aside>
"""

def func(nums):
    ptr = 0

    for fast_ptr in range(len(nums)):
        if nums[fast_ptr] != 0:
            nums[ptr], nums[fast_ptr] = nums[fast_ptr], nums[ptr]
            ptr += 1


nums = [0, 1, 0, 3, 12]

ans = func(nums)
print(ans)
print(nums)
