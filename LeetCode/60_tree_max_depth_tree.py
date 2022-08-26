from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_count = 0
        stack = [(1, root)]

        while len(stack) > 0:
            (depth, node) = stack(len(stack)-1)
            if node is not None:
                max_count = max(max_count, depth)
                stack.append((depth+1, node.left))
                stack.append((depth+1, node.right))
        
        return max_count
    
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if root == None: # == for object values
            return 0
        
        left_height = self.maxDepthRecursive(root.left)
        right_height = self.maxDepthRecursive(root.right)
        return max(left_height, right_height) + 1



        
"""
This problem is poorly defined in my opinion.

By definition, the maximum depth of a binary tree is the maximum number of steps to reach a leaf node from the root node.

So if a root node is none, or the children are none, the depth is 0.

Runtime is O(N) time for all nodes and space is O(N) stack traces for max depth
Middle case for tree search space is O(lg2N)
"""
        