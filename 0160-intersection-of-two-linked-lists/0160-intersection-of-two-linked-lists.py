# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Bu fonksiyon, verilen bağlı listenin uzunluğunu döndüren yardımcı bir fonksiyondur.
    def find_len(self, head: ListNode):
        i = 0
        node = head
        # Listeyi baştan sona kadar gez
        while node:
            i += 1  # Uzunluğu artır
            node = node.next  # Sonraki düğüme geç
        return i  # Toplam uzunluğu döndür

    # Bu fonksiyon, iki bağlı listenin kesişim noktasını bulur.
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Her iki listenin uzunluğunu hesapla
        len_a = self.find_len(headA)
        len_b = self.find_len(headB)

        # Daha uzun olan listeyi kısalt
        while len_a > len_b:
            headA = headA.next  # A listesinde bir adım ilerle
            len_a -= 1  # A listesinin uzunluğunu bir azalt
        while len_b > len_a:
            headB = headB.next  # B listesinde bir adım ilerle
            len_b -= 1  # B listesinin uzunluğunu bir azalt

        # İki listeyi gez ve kesişim noktasını bul
        while headA and headB:
            if (headA == headB):  # Kesişim noktası bulundu
                return headA
            headA = headA.next  # A listesinde bir adım ilerle
            headB = headB.next  # B listesinde bir adım ilerle

