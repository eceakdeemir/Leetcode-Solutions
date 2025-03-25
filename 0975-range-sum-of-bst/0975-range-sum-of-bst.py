# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []
        total = 0
        def traversal(node):
            if node:
                traversal(node.left)
                traversal(node.right)
                result.append(node.val)
        traversal(root)
        for i in result:
            if i >= low and i <= high:
                total += i
        return total