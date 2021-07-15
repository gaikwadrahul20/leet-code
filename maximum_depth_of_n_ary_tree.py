"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''Recursive'''
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        max_depth = 0
        
        for child in root.children:
            max_depth = max(self.maxDepth(child), max_depth)

        return max_depth + 1


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''Iterative'''
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        max_depth = -1
        
        for child in root.children:
            height = self.maxDepth(child)
            if height >= max_depth:
                max_depth = 1 + height

        return max(max_depth, 1)