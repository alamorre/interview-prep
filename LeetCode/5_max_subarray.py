from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if current < 0 and num > current:
                current = num 
            else: 
                current += num 
            
            if current > max_sum:
                max_sum = current
        
        return max_sum
                