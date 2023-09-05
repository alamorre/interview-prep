def return_greater(a: any, b: any):
    if a > b: return a
    elif b > a: return b
    else: return None

def bin_search(lst: list, elem: any):
    if len(lst) == 0: return 0
    left, right = 0, len(lst) - 1
    
    while left < right:
        mid = (left + right) // 2
        if return_greater(elem, lst[mid]) == elem: left = mid + 1
        elif return_greater(elem, lst[mid]) == lst[mid]: right = mid - 1
        else: return mid
    
    if return_greater(lst[left], elem) == elem: return left+1 
    else: return left

def bin_sort(lst: list):
    new_lst = []
    while len(lst) > 0:
        elem = lst.pop(0)
        i = bin_search(new_lst, elem)
        new_lst.insert(i, elem)
    return new_lst

print(bin_sort(lst=[5,6,8,2,3,1,2,5,6,7,9,8,0]))