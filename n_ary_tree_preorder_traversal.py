"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''Recursive'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        result = [root.val]
        for child in root.children:
            result.extend(self.preorder(child))
        return result
            
'''Iteraive'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if root is None:
            return []
        stack = collections.deque()
        stack.append(root)
        result = []
        head = root
        while stack:
            current = stack.pop()
            result.append(current.val)
            index = len(current.children) - 1
            while index >= 0:
                stack.append(current.children[index])
                index -= 1
        return result
            