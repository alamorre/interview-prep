from typing import List
import pprint 

SIZE = 100

# To start, this hash-set will support ints
# It will support 1 million keys
# If a collision occurs, we binary insert it in a sorted spot
# We will have a get method, to get the value for some key - or None
# We will have a set method, to set the value for some key/value pair
# Gets will be O(lg_n/10^6)
# Sets will be O(lg_n/10^6)

# List one is for all the spots
# List two is for the collided keys
# List three is to store the key/value pair
class HashTable():
    def __init__(self):
        self.hash_table: List[List[List[int]]] = [[]] * SIZE

    def __binary_insert_find_index(self, new_key_val: List[int], key_val_list: List[List[int]]) -> int:
        # Return the index to insert into list at
        low = 0
        high = len(key_val_list) - 1 
        
        while low <= high:
            if low == high:
                if new_key_val[0] < key_val_list[low][0]:
                    return low # apple will push banana to the right!
                elif new_key_val[0] == key_val_list[low][0]:
                    key_val_list[low][1] = new_key_val[1] # Overwrite, insert nothing
                    return None 
                else:
                    return low + 1 

            mid = (low + high) // 2
            if new_key_val[0] == key_val_list[mid][0]: # Overwrite, insert nothing
                key_val_list[mid][1] = new_key_val[1]
                return None 
            elif new_key_val[0] < key_val_list[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def set(self, key_val: List[int]): # Assume valid input
        key = key_val[0] % SIZE
        new_kv_list = self.hash_table[key].copy() # Mod math is done here, perfect!
        index = self.__binary_insert_find_index(key_val, new_kv_list)
        if index != None:
            # Insert key_val on purpose because you want the distinct (not flattened) keys
            self.hash_table[key] = new_kv_list[:index] + [key_val] + new_kv_list[index:]    

    def get(self, key: int) -> int:
        flat_key = key % SIZE
        for kv in self.hash_table[flat_key]:
            if key == kv[0]: # compare with the real key ;)
                return kv[1]
        return None

    def print(self):
        pprint.pprint(self.hash_table)

hash_table = HashTable()
hash_table.set([99, 1])
hash_table.set([99, 2])
hash_table.set([199, 1])
hash_table.set([299, 2])
hash_table.set([299, 3])
hash_table.set([298, 1])
hash_table.print()

val_1 = hash_table.get(99) # 2
val_2 = hash_table.get(298) # 1
val_3 = hash_table.get(1) # None
print(val_1, val_2, val_3)