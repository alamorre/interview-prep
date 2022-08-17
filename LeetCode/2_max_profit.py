from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        trailing_min = 10 ** 5
        max_profit = 0
        
        for i in range(0, len(prices)):
            price = prices[i]
            if price < trailing_min:
                trailing_min = price
            else:
                temp_profit = price - trailing_min
                if temp_profit > max_profit:
                    max_profit = temp_profit
        
        return max_profit
        
        