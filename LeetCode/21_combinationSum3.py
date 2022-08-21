from typing import List 

def combinationSum3(k: int, n: int) -> List[List[int]]:
    candidates = [i for i in range(1, 10)]
    results = []
    
    def backtrack(remain, curr, start):
        if remain == 0 and len(curr) == k:
            results.append(list(curr))
            return 
        elif remain < 0 or len(curr) == k:
            return 

        for i in range(start, len(candidates)):
            new_curr = curr + [candidates[i]]
            backtrack(remain - candidates[i], new_curr, i+1)

    backtrack(n, [], 0)
    return results
    


print(combinationSum3(9, 45))