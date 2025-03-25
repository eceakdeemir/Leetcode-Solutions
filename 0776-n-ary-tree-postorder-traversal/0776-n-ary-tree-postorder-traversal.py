"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def traversal(node):
            if node:
                for child in node.children:
                    traversal(child)
                result.append(node.val)
        traversal(root)
        return result