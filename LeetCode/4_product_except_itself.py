from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_of_i = []
        for i in range(0, len(nums)):
            if i == 0:
                left_of_i.append(1)
            elif i == 1:
                left_of_i.append(nums[i-1])
            else:
                left_of_i.append(nums[i-1] * left_of_i[i-1])
        
        right_nums_copy = nums.copy()
        right_nums_copy.reverse()

        right_of_i = []
        for i in range(0, len(right_nums_copy)):
            if i == 0:
                right_of_i.append(1)
            elif i == 1:
                right_of_i.append(right_nums_copy[i-1])
            else:
                right_of_i.append(right_nums_copy[i-1] * right_of_i[i-1])
        
        right_of_i.reverse()
        
        answer = []
        for i in range(0, len(left_of_i)):
            left = left_of_i[i]
            right = right_of_i[i]
            answer.append(left * right)
        
        return answer
        
nums = [1,2,3]
answer = Solution().productExceptSelf(nums=nums)
print(answer)