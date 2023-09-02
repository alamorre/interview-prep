# Sets without reference types
data = {'a','b','c'}
data.add('d')
print('\'d\' is true: ', 'd' in data) # True

class Node():
    def __init__(self, val: str, left, right) -> None:
        self.val = val
        self.left = left 
        self.right = right

# Sets without reference types
n1 = Node('a', None, None)
n1_ref = n1
n1_clone = Node('a', None, None)
data = {n1}
print('Ref is true: ', n1_ref in data) # True
print('Clone is false: ', n1_clone in data) # False
data.remove(n1_ref)
print('n1 is gone (ie False)', n1 in data) # False
