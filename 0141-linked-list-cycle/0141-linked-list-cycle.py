# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        new = set()
        node = head
        while node:
            if node in new:
                return True
            new.add(node)
            node = node.next
        return False
