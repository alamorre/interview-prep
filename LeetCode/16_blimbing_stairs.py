class Solution:
    def climbStairs(self, n: int) -> int:
        counts = [1, 2]
        if n == 1: # base case
            return 1
        for i in range(3, n + 1):
            counts.append(counts[0] + counts[1])
            counts.pop(0)
        return counts[1]

print(Solution().climbStairs(3))

"""
Tips: 
.pop() requires an index
Remember the edge cases
"""