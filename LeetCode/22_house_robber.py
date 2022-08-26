from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0, 0, 0]
        global_max = 0
        
        for i in range(0, len(nums)):
            # Base-case: get the first hours
            if i == 0:
                dp[3] = nums[0]
                global_max = nums[0]
            
            else:
                four_ago = dp[0]
                three_ago = dp[1]
                # Two ago can only pull from 4 ago
                two_ago = four_ago + nums[i-2] if i-2 >= 0 else 0
                one_ago = dp[3]
                
                local_max = max(
                    one_ago,
                    nums[i] + two_ago,
                    nums[i] + three_ago,
                )
                global_max = max(global_max, local_max)
                
                dp.append(local_max)
                dp.pop(0)
        
        return global_max