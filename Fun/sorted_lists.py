# ~~~~~ NATIVE SORTED LIST ~~~~~
import bisect 

a = [1, 2, 3, 4, 5] 
bisect.insort(a, 3) # STILL O(N)
print(a)

i = bisect.bisect_left(a, 4.5)
j = bisect.bisect_right(a, 4.5)
print(i, j)

# pump out a reverse binary sorted list
def binsert(arr, item):
    low, high = 0, len(arr)-1
    while low <= high:
        if low == high:
            if arr[low] > item: return low+1
            else: return low
        mid = (low + high) // 2
        if arr[mid] == item: return mid
        elif arr[mid] > item: high = mid-1
        else: low = mid+1
    return 0

def reverse_binsort(arr):
    new_arr = []
    while len(arr) > 0:
        item = arr.pop(-1)
        i = binsert(new_arr, item)
        new_arr.insert(i, item)
    return new_arr

print(reverse_binsort([3,4,7,5,6]))

