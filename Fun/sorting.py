lst_1 = [3,6,8,9,4,2,1,5,7,0]
lst_2 = [5,67,8,9,5,3,1,1,3,5,6,78,9,0,0,8,6,4,3]

def binsert(lst: list, x: any) -> list:
    low, high = 0, len(lst)-1
    while low <= high:
        if low == high: #[1,3,5] think 2,3,4 scenarios
            if x <= lst[low]: return low 
            else: return low+1
        mid = (high + low)//2
        if lst[mid] < x: low = mid+1
        elif x < lst[mid]:high = mid-1
        else: return mid
    return low

print(binsert([], 1))
print(binsert([2], 1))
print(binsert([2], 3))
print(binsert([1,3], 2))
print(binsert([0,1,2,3,4,5,6], 4))

def sort(lst: list) -> list:
    sol = []
    while len(lst) > 0:
        x = lst.pop()
        i = binsert(sol, x)
        sol.insert(i, x)
    return sol

print(sort(lst_1))
print(sort(lst_2))