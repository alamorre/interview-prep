import math 
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(0)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3

string = Codec().serialize(root)
i = 45
print(len(string))
while i <= len(string)+1:
    print(string[i-45:i-30], string[i-30:i-15], string[i-15:i], )
    i += 45
node = Codec().deserialize(string)
print(root.val, root.left.val, root.right.val)

"""
To handle negative representation, just use a sign bit at the front
0 for pos and 1 for neg, add that into base10 logic, then make deserialize by 15 bits
You're done!

This code works on 

This doesn't account for indexes. Since there can be multiple nodes with val == 1 for instance.
We can essentially capitalize on the order. Our left and right vals can be left and right pointers
i.e. indexes.
"""