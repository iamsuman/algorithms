
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list:
        res = []

        def traversal(node: Node):
            if node:
                if node.children:
                    for child in node.children:
                        traversal(child)
                res.append(node.val)

        traversal(root)
        return res

