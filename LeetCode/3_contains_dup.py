from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in range(0, len(nums)):
            num = nums[i]
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False
        