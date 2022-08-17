from typing import List 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # Cannot look forward if positive
            # Looking forward is needed to remove dups
            if nums[i] > 0: 
                break
            # if first elem or not duplicate i
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set() # tally which complements you've seen
        j = i + 1
        while j < len(nums): # j = 3
            complement = -nums[i] - nums[j] # 2
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                # skip over duplicate j in sorted array
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
        # Dumb tip: while loops are needed for if you're skipping indexes 
        # Don't use for loops

"""
This is really cool, we can use this whenever we need
non-duplicated criteria in an array.
"""

print(Solution().threeSum([-1,0,1,2,-1,-4]))