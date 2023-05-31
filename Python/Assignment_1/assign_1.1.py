"""<aside>
💡 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][

</aside>
"""

def func(nums, target):
    map = {}
    
    for i, num_1 in enumerate(nums):
        num_2 = target - num_1
        
        if num_2 in map:
            return [map[num_2], i]
        
        map[num_1] = i
    
    return []

