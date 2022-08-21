from typing import List 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        # count = 7; 
        # dp = [inf, inf, inf, inf, inf, inf, inf, inf]
        dp[0] = 0
        # dp = [0, inf, inf, inf, inf, inf, inf, inf]
        
        for coin in coins: # [2, 5]
            # coin = 2
            for x in range(coin, amount + 1): # 2 to 7
                #           inf.   dp[2-2] + 1 = 1
                dp[x] = min(dp[x], dp[x - coin] + 1)
                # dp[2] = 1
        return dp[amount] if dp[amount] != float('inf') else -1 

"""
Tips: 
"""

amount = 10
coins = [1, 3, 2]

memo = [float('inf')] * (amount+1) # 0 to amount
memo[0] = 0 # base case
# We have a list of least-optimal answers and a base case

# For each coin, see where it can apply and make the solution better
for coin in coins:
    for i in range(coin, amount + 1): # from coin to amount
        memo[i] = min(memo[i], 1 + memo[i - coin]) # see ithe coin can lower the count here
answer = memo[amount] if memo[amount] < float('inf') else -1
print(answer)
    
