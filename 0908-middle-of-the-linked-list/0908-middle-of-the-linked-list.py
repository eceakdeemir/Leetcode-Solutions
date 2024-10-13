# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> Optional[ListNode]:
        lenght = self.len_list(head)
        if lenght == 1:
            return head
        for i in range(lenght // 2):
            head = head.next
        return head

    def len_list(self, head: ListNode) -> int:
        i = 0
        tmp = head
        while (tmp != None):
            i += 1
            tmp = tmp.next
        return i