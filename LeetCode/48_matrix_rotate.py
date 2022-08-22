from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0 # start at outermost ring
        
        while i < n // 2: 
            # Rotate the ring
            for j in range(i, n-i-1): # n - 1
                # use temps
                temp_tl = matrix[i][j] # store what we're writing over
                temp_tr = matrix[j][n-i-1] 
                temp_br = matrix[n-i-1][n-j-1] 
                temp_bl = matrix[n-j-1][i]
                matrix[j][n-i-1] = temp_tl
                matrix[n-i-1][n-j-1] = temp_tr
                matrix[n-j-1][i] = temp_br
                matrix[i][j] = temp_bl
            i += 1

"""
Flashed in 1 try on video - atta be!!!
Your use of temps is very clear. Do that in future questions to think more clearly.
"""