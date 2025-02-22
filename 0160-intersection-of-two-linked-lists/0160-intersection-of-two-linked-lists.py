# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def find_len(self, head: ListNode):
        i = 0
        node = head
        while node:
            i += 1
            node = node.next
        return i

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = self.find_len(headA)
        len_b = self.find_len(headB)

        while len_a > len_b:
            headA = headA.next
            len_a -= 1
        while len_b > len_a:
            headB = headB.next
            len_b -= 1
        
        while headA and headB:
            if (headA == headB):
                return headA
            headA = headA.next
            headB = headB.next
