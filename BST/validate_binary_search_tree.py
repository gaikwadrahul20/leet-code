# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        path = self.preorder_traversal(root)
        max = path[0]
        for i in range(len(path)-1):
            if path[i]>=path[i+1]:
                return False
        return True
        
    def preorder_traversal(self, root):
        path = []
        if root is None:
            return []
        path = path + self.preorder_traversal(root.left)
        path.append(root.val)
        path = path + self.preorder_traversal(root.right)
        return path