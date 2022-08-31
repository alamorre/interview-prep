from typing import List 

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        overlap, count = -float('inf'), 0
        
        for i in range(0, len(intervals)):
            interval = intervals[i]
            if interval[0] < overlap: # i.e. overlap
                count += 1
                overlap = min(overlap, interval[1])
            else: 
                overlap = max(overlap, interval[1])
                
        return count

"""
This is technically DP where we store the last endpoint / solution.
Then we cross-reference with new start and store a new optimum for this index.
"""

# For event interval i
# you need to add i and likely increase the end_overlap
# OR remove the item and use a lower overlap
#                  1
#         [1,2],[2,3],[3,4]
#         lowest = 0
        