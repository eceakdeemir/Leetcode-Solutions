# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # En küçük stringi tutmak için başlangıç değeri olarak "~" verilir.
        # "~" karakteri, 'a'-'z' harflerinden sözlük sırasına göre daha büyüktür.
        self.smallest = "~"

        # Derinlik öncelikli arama (DFS) fonksiyonu tanımlanıyor.
        def dfs(node, path):
            # Eğer mevcut düğüm yoksa (None), bu yolu durdur.
            if not node:
                return

            # Düğümün sayısal değeri 'a'-'z' harfine çevrilir ve yolun başına eklenir.
            # Çünkü biz yapraktan köke doğru string oluşturuyoruz.
            path = chr(ord('a') + node.val) + path

            # Eğer bu bir yaprak düğümse (hiç çocuğu yoksa):
            if not node.left and not node.right:
                # Bu yoldan oluşan string daha önceki en küçük stringten küçükse:
                if path < self.smallest:
                    # En küçük stringi güncelle
                    self.smallest = path

            # Sol çocuğa doğru DFS ile devam et
            dfs(node.left, path)
            # Sağ çocuğa doğru DFS ile devam et
            dfs(node.right, path)

        # DFS fonksiyonunu kök düğümden başlat
        dfs(root, "")

        # Tüm yapraklardan elde edilen yollar arasında en küçük olanı döndür
        return self.smallest
