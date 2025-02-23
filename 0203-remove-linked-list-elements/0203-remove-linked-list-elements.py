# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Listenin başındaki düğümleri kontrol et ve 'val' ile eşleşenleri sil
        while head and head.val == val:
            head = head.next  # Başta 'val' değerine sahip düğümleri geç

        # Yeni bir baş başlatıyoruz
        new_head = head
        
        # Listenin geri kalanını kontrol et
        while new_head and new_head.next:
            # Eğer bir sonraki düğümde 'val' değeri varsa, o düğümü sil
            if new_head.next.val == val:
                new_head.next = new_head.next.next  # 'new_head.next' düğümünü atla
            else:
                new_head = new_head.next  # 'new_head' bir adım ileri git
                
        # Güncellenmiş başı döndür
        return head
