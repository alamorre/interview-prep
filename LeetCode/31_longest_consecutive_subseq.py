class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)
        # Didn't think you could set the entire list 
        # Also didn't recall you can iterate through the 
        for num in num_set: # O(n)
            # This makes is not O(N^2)
            # Will only run on bottom nums
            if num - 1 not in num_set: 
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

"""
It is O(2n). As shown below, you'll double check a few, but that's fine.
[1,2,3, 5,6,7, 9,10,11]
 ^ ^ ^
   ^ 
     ^
"""