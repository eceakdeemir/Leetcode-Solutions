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
        tmp = head
        for i in range(lenght // 2):
            tmp = tmp.next
        return tmp

    def len_list(self, head: ListNode) -> int:
        i = 0
        tmp = head
        while (tmp != None):
            i += 1
            tmp = tmp.next
        return i