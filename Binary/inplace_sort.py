def binaryInset(elems, insert, wall):
    low = 0
    high = wall 

    while low <= high:
        if low == high:
            if insert <= elems[low]:
                elems.insert(low, insert)
                return
            else:
                elems.insert(low+1, insert)
                return
        else:
            mid = (low + high) // 2
            if elems[mid] == insert:
                elems.insert(mid, insert)
                return
            elif elems[mid] < insert: # 
                low = mid + 1
            else:
                high = mid - 1
    
    if high < low:
        elems.insert(0, insert)
    

def inplaceSort(nums):
    for i in range(0, len(nums)):
        elem = nums.pop(i) # 0 then 1 ...
        binaryInset(nums, elem, i-1) # -1 bc elem was taken out
    return nums

nums = [3,2,1,0,5,9,7]
print(inplaceSort(nums=nums))
