from typing import List 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(0, len(nums)):
            num = nums[i]
            max_so_far = max(num, max_so_far * num, min_so_far * num)
            min_so_far = min(num, max_so_far * num, min_so_far * num)
            result = max(result, max_so_far)
        
        return result

print('Max', Solution().maxProduct([-2,0,-1]))