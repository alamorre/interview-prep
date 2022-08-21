import pprint
from typing import List 

def combo_twos(nums: List[int]):
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            print(nums[i], nums[j])

combo_twos([1,2,3,4,5])

def combo_threes(nums: List[int]):
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                print(nums[i], nums[j], nums[k])

combo_threes([1,2,3,4,5])

# O(c^n)
def unique_combos_len_n(candidates: List[int], n:int):
    results = []

    def backtrack(current, start):
        if len(current) == n:
            results.append(list(current))
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(current, i+1)
            current.pop(len(current) - 1)

    backtrack([], 0)
    return results

pprint.pprint(unique_combos_len_n([1,2,3,4,5,6,7,8,9], 4))


def repeat_combos_len_n(candidates: List[int], n:int):
    results = []

    def backtrack(current, start):
        if len(current) == n:
            results.append(list(current))
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(current, i)
            current.pop(len(current) - 1)

    backtrack([], 0)
    return results

pprint.pprint(repeat_combos_len_n([1,2,3,4,5,6,7,8,9], 4))