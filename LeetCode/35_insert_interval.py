from typing import List 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals starting before newInterval
        while idx < n and intervals[idx][0] < new_start:
            output.append(intervals[idx])
            idx += 1
            
        # start1             end1     start2 end2 start3           end3 start4 end4
        #        newstart                                 newend
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)
        
        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # If the next index needs to be merged, merge
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            # else add the intervals
            else:
                output.append(interval)
                
        return output
            


"""
Tip: Edit last elem easy with [-1] index
Greedy algorithm. Add elem by elem until overlap. Then edit last elem accordingly.
"""

