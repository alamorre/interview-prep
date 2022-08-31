# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid_subtree(node, be_under=float('inf'), be_over=-float('inf')):
            # Base case, True if at end
            if not node: return True
            elif be_under <= node.val or node.val <= be_over:
                # Fail if left node is over parent
                return False
            
            l_valid = valid_subtree(node.left, node.val, be_over)
            r_valid = valid_subtree(node.right, be_under, node.val)
            return l_valid and r_valid
        
        return valid_subtree(root)
            
            
"""
WHAT I GOT WRONG:
I need to have a low and high to keep track of. Not just a be_under OR over
Tip: thre defaults make the code more concise

You got most of the concept, but you need to be aware of the past limits too
You don't need to do a max() / min() type of assignment if it's a valid BST with no equiv' values. 
"""