# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfsCheck(n1, n2):
            if not n1 and not n2: # Reached past leaf - good
                return True
            elif (n1 and not n2) or (not n1 and n2): # One is longer - bad
                return False
            elif n1.val != n2.val: # Values are different - bad
                return False
            return dfsCheck(n1.left, n2.left) and dfsCheck(n1.right, n2.right)

        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            # Return true if valid subtree
            if node.val == subRoot.val and dfsCheck(node, subRoot):
                return True
            # Check left and right then
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False
        
        