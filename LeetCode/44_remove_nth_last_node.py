# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        for i in range(0, n): # 1 <= n <= sz so no edge cases
            current = current.next
        laggard = None
        
        # We can move into none that's fine!
        while current:
            current = current.next
            laggard = laggard.next if laggard else head
           
        
        if not laggard: # Edge case of n = length of list
            head = head.next # Move the head down
        else:
            laggard.next = laggard.next.next
        
        return head
        
# List of nodes, int n
# Remove nth node from end of list

# Trivial solution: Index all nodes, and remove it on second pass
# while current: i++; current = current.next;
# while current: i++;  if i == index: remove node

# What we can do, is store a node laggin behind current by n:
#     Once there is no more next, do the swap