# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        middle = fast = head
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        
        prev = None
        reverse = middle
        while reverse:
            tmp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = tmp
        reverse = prev # Now 5
        
        # 1->2->3->4 and 6->5->4
        # Assume l1 is equal or longer
        first, second = head, reverse
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp
            # Ohhhh do two in each while loop
            tmp = second.next
            second.next = first
            second = tmp
            
        return head

""""
The slow and fast pointer method is clever for determining list sections and indexes.
"""