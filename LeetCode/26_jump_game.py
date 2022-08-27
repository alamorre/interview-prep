from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prior_jump = 1
        
        for i in range(0, len(nums)-1):
            # use current jump, or prior jump 
            max_jump = max(nums[i], prior_jump-1) 
            # If you cannot jump and not at end
            if max_jump <= 0:
                return False
            prior_jump = max_jump
        
        return True
        
        

# [2,3,1,1,4]
#  2 
#    3 or 2-1 = 3
#      1 or 3-1 = 2
#        1 or 2-1 = 1 (return false if it's "0or0" before the end)
         
# [3,2,1,0,4]
#  3 2 1 0