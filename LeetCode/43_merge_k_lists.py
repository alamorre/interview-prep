class Solution:
    def getMin(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Return the index and value
        global_min = float('inf')
        index = -1
        for i in range(0, len(lists)):
            if lists[i].val < global_min: 
                global_min = lists[i].val
                index = i
        return index
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Groom the list
        tmp_lists = []
        for lst in lists: 
            if lst: tmp_lists.append(lst)
        lists = tmp_lists
        if lists == []: return None
        
        ans = []
        while lists != []:
            min_index = self.getMin(lists)
            min_node = lists[min_index]
            
            if ans == []:
                ans.append(min_node)
            else:
                prev_node = ans[len(ans) - 1]
                prev_node.next = min_node
                ans.append(min_node)
            
            if not min_node.next:
                lists.pop(min_index)
            else:
                lists[min_index] = min_node.next
        
        return ans[0]