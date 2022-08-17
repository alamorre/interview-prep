from typing import List 

def two_sum(nums: List[int], target: int) -> List[int]:
    pairs = {}

    # Go throught and k:v the other number needed and index
    for i in range(0, len(nums)):
        num = nums[i] # For sanity
        pairs[target - num] = i
    
    # Go through nums again, see which key exists
    # If the i value is different, return both
    for i in range(0, len(nums)):
        num = nums[i]
        if pairs.get(num, False) and i != pairs[num]:
            return [pairs[num], i]

    # We assume there is always a pair.

nums = [-1,7,3,9,-10]
target = 2
pair = two_sum(nums, target)
print(pair)