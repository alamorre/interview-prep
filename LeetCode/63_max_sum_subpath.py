class Solution:
    def maxPathSum(self, root):
        def maxAtNode(node):
            nonlocal max_count
            if node == None:
                return 0

            # Run against 0 because we can exclude negative subpaths (ofc)
            left_sum = max(maxAtNode(node.left), 0)
            right_sum = max(maxAtNode(node.right), 0)

            sum_without_parent = left_sum + right_sum + node.val
            max_count = max(max_count, sum_without_parent)
            
            return node.val + max(left_sum, right_sum)

        max_count = -float('inf') # For negative nodes
        maxAtNode(root)
        return max_count


"""
Tip: nonlocal allows you to break variable scoping up one level

To not involve one option in your recursion, just assign it against the global max in the function
 - returning nothing.
If you want it as an option in your recursion, return it for higher-calculations.
"""