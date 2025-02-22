# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        new_head = head
        while new_head and new_head.next:
            if new_head.next.val == val:
                new_head.next = new_head.next.next
            else:
                new_head = new_head.next
        return head