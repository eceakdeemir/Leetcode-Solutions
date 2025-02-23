# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Yeni bir dummy node (sentinel) oluştur ve başı ona bağla
        new = ListNode(0)
        new.next = head

        # 'tmp' geçici bir işaretçi, işlemleri başlatacağımız yer
        tmp = new

        # Listenin sonuna kadar giderek her iki ardışık düğümün yerini değiştir
        while (tmp.next and tmp.next.next):
            # İlk iki düğümü al
            first = tmp.next
            second = tmp.next.next

            # İlk düğümü ikinci düğümün sonrasına bağla
            first.next = second.next
            # İkinci düğümü ilk düğümün öncesine bağla
            second.next = first
            # 'tmp' düğümünü ikinci düğüme bağla
            tmp.next = second

            # Bir sonraki iterasyon için 'tmp'yi güncelle
            tmp = first
        
        # Yeni başı döndür (new düğümü sadece yardımcı düğüm olduğu için new.next döndürülür)
        return new.next


        


        