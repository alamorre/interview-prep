from typing import List 
import math 

def countBits(self, n: int) -> List[int]:
        dp = {0:0} # Keep your base case concise! For the min reason...
        
        for num in range(1, n + 1):
            exponent = math.floor(math.log2(num))
            prior = num - (2**exponent)
            dp[num] = 1 + dp[prior] 
        
        return dp.values()