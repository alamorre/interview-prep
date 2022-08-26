from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:
            left_val = height[left]
            right_val = height[right]

            area = min(left_val, right_val) * (right - left)
            max_area = max(area, max_area)

            if left_val <= right_val:
                left += 1
            else:
                right -=1

        return max_area
        