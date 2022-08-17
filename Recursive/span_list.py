from typing import List
import pprint

def list_removing_each_item(nums: List[int]) -> List[List[int]]:
    list_of_lists = []
    for i in range(0, len(nums)):
        temp = nums.copy()
        del temp[i]
        list_of_lists.append(temp)
    return list_of_lists

def span_list_to_threes(number_sets: List[List[int]]) -> List[List[int]]:
    if len(number_sets[0]) == 3:
        return list(filter(lambda x: sum(x) == 0, number_sets))

    new_number_sets = []
    for number_set in number_sets:
        new_number_sets = new_number_sets + list_removing_each_item(number_set)

    return span_list_to_threes(new_number_sets)
    
def remove_diplicate_lists(lists: List[List[str]]) -> List[List[str]]:
    new_lists = []
    for l in lists:
        l.sort()
        if not any(l == other_l for other_l in new_lists):
            new_lists.append(l)
    return new_lists

example = [1, 2, -3, 4, -5, 6]
# new_list = list_removing_each_item(example)
new_list = span_list_to_threes([example])
concise_sol = remove_diplicate_lists(new_list)
pprint.pprint(concise_sol)

# Basic for loop
for i in range(0, len(example)):
    print(i, example[i])