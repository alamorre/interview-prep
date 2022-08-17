from typing import List 
import time

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = nums[0]
        right = nums[len(nums) - 1]
        if left <= right:
            return nums[0]
        
        # if we just focus on right side
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            num = nums[mid]
            print(mid, num, low, high)
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if left > num:
                high = mid - 1
            else:
                low = mid + 1

print(Solution().findMin(nums=[1,2,3,4,5]))

# 3,4,5,1,2
# 