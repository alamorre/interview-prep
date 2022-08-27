class Solution:
    def binaryInsert(self, nodes, node) -> int:
        low = 0
        high = len(nodes) - 1
        
        while low <= high:
            if low == high:
                return low if node.val <= nodes[low].val else low+1
                
            mid = (low + high) // 2
            if nodes[mid].val == node.val:
                return mid
            elif node.val < nodes[mid].val:
                high = mid - 1
            elif nodes[mid].val < node.val:
                low = mid + 1

        if high == -1:
            return 0
        
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        ans = [[root.val]]
        queue = [[root]]
        
        while len(queue) > 0:
            level = queue.pop(0)
            
            new_level = [] 
            for node in level:
                if node.left:
                    # index = self.binaryInsert(new_level, node.left)
                    new_level.append(node.left)
                if node.right:
                    # index = self.binaryInsert(new_level, node.right)
                    new_level.append(node.right)
            
            if len(new_level) > 0:
                ans.append([node.val for node in new_level])
                queue.append(new_level)
        
        return ans 