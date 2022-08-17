import math

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        top_col = math.ceil(math.log10(columnNumber) // math.log10(26)) - 1
        
        letter_nums = []
        number = columnNumber #1000
        for i in range(top_col, -1, -1): #2,1,0
            base = number // 26**i
            letter_nums.append(base)
            remainder = number % 26**i
            number = remainder
        
        sol = ''
        for i in range(0, len(letter_nums)):
            letter = letter_nums[i]
            ascii_shift = 64 if i == 0 else 65
            char = chr(letter + ascii_shift)
            sol = sol + char
        
        return sol

# Not solved

sol = Solution()
print(sol.convertToTitle(1))
print(sol.convertToTitle(26))