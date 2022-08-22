from typing import List 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        delete_col = False
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, rows):
            if matrix[i][0] == 0:
                delete_col = True
            # Start at 1 so you don't 0 out m[0,0]
            # example: if BL is 0, now TL is and top row gets deleted
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
            
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(0, cols):
                matrix[0][j] = 0

        if delete_col:
            for i in range(0, rows):
                matrix[i][0] = 0