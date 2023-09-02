import pprint 

def make_all_sub_arrays(nums):
    results = []
    for i in range(0, len(nums)): 
        for j in range(i, len(nums)): 
            sub = ''
            for k in range(i, j + 1):
                sub += str(nums[k])
            if len(sub) > 0:
                results.append(sub)
    return results

pprint.pprint(make_all_sub_arrays([1,2,3,4]))

def rec_arrays(string, sol):
    if string == "": return string
    for i in range(0, len(string)):
        sol.append(string[0:i+1]) # honours -1 and that's already in there
    rec_arrays(string[1:], sol)
sol = [] 
rec_arrays('banana', sol)
print(sol)
