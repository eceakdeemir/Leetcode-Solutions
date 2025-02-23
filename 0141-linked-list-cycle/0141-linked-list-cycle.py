# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast ve slow'u baştan (head) aynı noktaya yerleştiriyoruz.
        fast = slow = head
        
        # fast ve slow'u, listenin sonuna kadar hareket ettiriyoruz.
        # fast her adımda iki ileriye gider, slow ise bir adımda bir ileriye gider.
        while fast and fast.next:
            # slow bir adım ilerler, fast ise iki adım ilerler.
            slow, fast = slow.next, fast.next.next
            
            # Eğer fast slow'a ulaşırsa, bu bir döngü olduğunu gösterir.
            if fast == slow:
                return True
        
        # Eğer fast listenin sonuna ulaşırsa ve slow ile aynı noktaya gelmezse,
        # bu listenin döngüsüz olduğunu gösterir.
        return False

