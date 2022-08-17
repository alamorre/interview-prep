from typing import List 

class Solution:
    def bin_search(self, nums: List[int], target: int) -> int: 
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            current = nums[mid]
            if target == current:
                return mid
            elif target > current:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        if nums[left_index] <= nums[right_index]:
            return self.bin_search(nums, target)
        
        max_index = None
        min_index = None
        
        while left_index < right_index:
            mid = (left_index + right_index) // 2
            current = nums[mid]
            
            if nums[mid-1] > nums[mid]:
                max_index = mid-1
                min_index = mid
                break
            elif nums[mid] > nums[mid+1]:
                max_index = mid
                min_index = mid+1
                break
            
            if nums[left_index] > nums[mid]:
                right_index = mid-1
            else:
                left_index = mid+1

        left = nums[0]
        right = nums[len(nums) - 1]
        max_val = nums[max_index]
        min_val = nums[min_index]

        left_nums = nums[0:max_index+1]
        right_nums = nums[min_index:len(nums)]

        print(max_index, min_index)
        print(left_nums, right_nums)

        if left <= target and target <= max_val:
            return self.bin_search(left_nums, target)
        else:
            right_sol = self.bin_search(right_nums, target)
            if right_sol >= 0:
                return max_index + 1 + right_sol
            return right_sol
    
                
print(Solution().search([7,8,1,2,3,4,5,6], 2))
print(Solution().search([3,1], 1))
