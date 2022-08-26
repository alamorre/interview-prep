from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case
        if p == None and q == None: # Got to the end!
            return True
        elif p == None and q != None: # Not balanced
            return False
        elif q == None and p != None: # Not balanced
            return False
        elif p.val != q.val: # Different node
            return False

        left_true = self.isSameTree(p.left, q.left)
        right_true = self.isSameTree(p.right, q.right)
        return left_true and right_true # Only true if both are

            
        