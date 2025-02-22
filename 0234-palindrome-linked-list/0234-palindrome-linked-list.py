# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_list = []
        new_head = head
        while (new_head):
            new_list.append(new_head.val)
            new_head = new_head.next
        if (new_list == new_list[::-1]):
            return True
        return False