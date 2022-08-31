class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Make sure p < q
        if q.val < p.val: return self.lowestCommonAncestor(root, q, p)
        
        """
        All values left of node are under root.
        All values right of node are over root.
        """
        node = root
        while node != None:
            if p.val <= node.val and node.val <= q.val:
                return node
            elif p.val < node.val and q.val < node.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
        return None

"""
Again, everything to the left is under root, everything right is over
Use you head, you could have had this knowing 
- all vals are unique
- p & q are both IN the tree and unique. Could have flashed in 20 seconds. 
"""