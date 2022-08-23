from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.M = len(board)
        self.N = len(board[0])
        self.board = board

        for i in range(0, self.M):
            for j in range(0, self.N):
                if self.backtrack(i, j, word):
                    return True
        
        return False

    def backtrack(self, row, col, suffix) -> bool:
        if len(suffix) == 0:
            return True
        elif row < 0 or self.M <= row or col < 0 or self.N <= col or \
            suffix[0] != self.board[row][col]:
            return False

        self.board[row][col] = '#'
        is_found = False
        if self.backtrack(row-1, col, suffix[1:]):
            is_found = True
        if self.backtrack(row, col-1, suffix[1:]):
            is_found = True
        if self.backtrack(row+1, col, suffix[1:]):
            is_found = True
        if self.backtrack(row, col+1, suffix[1:]):
            is_found = True
        self.board[row][col] = suffix[0]

        return is_found
        

