# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# bottom up approach
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    
# Top down approach    
class Solution:
    def maximum_depth(self, root, level):
        if root is None:
            return 0
        if level > self.answer:
            self.answer = level
        self.maximum_depth(root.left, 1 + level)
        self.maximum_depth(root.right, 1+ level)
    
    def maxDepth(self, root: TreeNode) -> int:
        
        self.answer = 0
        self.maximum_depth(root, 1)
        return self.answer

# BFS solution
# DFS solution