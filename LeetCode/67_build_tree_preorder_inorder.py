class Solution:
    def buildTree(self, preorder, inorder):
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right: return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1 # Move to next (e.g. 3 to 9)
            # This index iter works because it builds entire left then entire right

            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            return root

        preorder_index = 0

        # build a hashmap to store value -> index relations
        inorder_index_map = {}
        for i in range(0, len(inorder)):
            inorder_index_map[inorder[i]] = i

        return array_to_tree(0, len(preorder) - 1)
            
            
"""
Tip: if you know all elems are unique, search for index in O(1) w/ a dict

It's important to know the traversal implications. Preorder still builds ENTIRE left before ANY of the right. That's why this iter+=1 through preorder is a safe assumption. 

ON time because you have to build out every node once
Avg case OlgN and worst case ON for an imbalanced tree
"""
                