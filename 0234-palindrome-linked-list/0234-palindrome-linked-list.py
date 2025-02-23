# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Bağlı listeyi bir diziye dönüştür
        new_list = []
        new_head = head
        # Listeyi baştan sona kadar gez ve değerleri new_list'e ekle
        while (new_head):
            new_list.append(new_head.val)  # Düğümün değerini ekle
            new_head = new_head.next  # Sonraki düğüme geç
        
        # Eğer liste, tersine eşitse palindromdur
        if (new_list == new_list[::-1]):
            return True
        
        # Eğer palindrom değilse, False döndür
        return False
