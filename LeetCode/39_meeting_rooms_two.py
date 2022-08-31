from typing import List 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def closestOpening(rooms, start):
            index, min_idle = -1, float('inf')
            for i in range(0, len(rooms)):
                idle = start - rooms[i] # 5 - 30 = -25
                if 0 <= idle and idle < min_idle:
                    min_idle = idle
                    index = i
            return index

        intervals.sort(key=lambda x: x[0]) # [[0,30],[5,10],[15,20]]
        rooms = [intervals[0][1]] # [30, 10]
        for i in range(1, len(intervals)):
            interval = intervals[i] # [15,20]
            open_index = closestOpening(rooms, interval[0])
            if open_index != -1: # return index of closest opening
                rooms[open_index] = interval[1] # Update co to endtime
            else:
                rooms.append(interval[1]) # Add conference room as endtime
        
        return len(rooms)
                
"""
Nested for loop of N^2 but can trim to NlgN with binary search for open time.
"""
        
# [[0,30],[5,10],[15,20]]
#  1: 30          
#         2: 10   2: 20