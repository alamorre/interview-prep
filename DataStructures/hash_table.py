# Declare a dictionary 
dict = {
    'Name': 'Zara', 
    'Age': 7, 
    'Class': 'First'
}

# Accessing the dictionary with its key
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])


"""
Notes:
Remember, collisions are kinda common.
Basically is uses hashing and the mod function to find it's spot in the set.
Once it's in the set, it uses a linked list to store collided elements.
It's basically O(n/number_of_slots) but nowadays number_of_slots is soo much it's like 1
Worst case it's O(N) but practically it's O(1).
Lengths of prime numbers assure all spots get filled, and rather evenly.

NOTE: Could you not implement the linked-list with an array of some-sort then binary-search with O(lg_n)???
Would be a good practice data-structure to make
Let's do it... see "hash_table_self_made.py" in this dir.
"""