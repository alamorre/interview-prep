from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Entire top row
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Right col - first row elem
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Bottom row - last col elem
            if up != down: # think about one row
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Left row - last row elem - first row elem
            if left != right: # think about one col
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
            
            # Do it all at once, then move everything in
            left += 1
            right -= 1
            up += 1
            down -= 1

        return result

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))