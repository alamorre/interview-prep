from typing import List 

def dfs_backtracking(nums: List[int], target: int):
    results = []
    def backtrack(remain: int, comb: List[int], start: int):
        # Base case, remain is 0
        if remain == 0:
            results.append(list(comb))
            return
        # Base case, remain < 0 (too high)
        elif remain < 0:
            return
        
        for i in range(start, len(nums)):
            comb.append(nums[i])
            backtrack(remain - nums[i], comb, i)
            comb.pop()
            # Cover the append and pop a bit more

    backtrack(target, [], 0)
    return results

def dfs_unique_backtracking(nums: List[int]):
    results = []
    def backtrack(curr_nums: List[int], remain_nums: List[int], start: int):
        # Base case, remain is 0
        if len(remain_nums) == 0:
            results.append(list(curr_nums))
            return
        
        for i in range(start, len(remain_nums)):
            new_remain_nums = remain_nums[0:i] + remain_nums[i+1:len(remain_nums)]
            backtrack(curr_nums, new_remain_nums, i) # Without that num
            backtrack(curr_nums + [remain_nums[i]], new_remain_nums, i) # With that num

    backtrack([], nums, 0)
    return results

print(dfs_backtracking([3,4,5], 8))
print(dfs_unique_backtracking([3,4,5]))