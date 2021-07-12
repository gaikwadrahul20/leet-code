# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root.val == val:
            return root
        if root.left and val < root.val:
            return self.searchBST(root.left, val)
        if root.right and val > root.val:
            return self.searchBST(root.right, val)
        return None


# Iterative 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        while root is not None and root.val != val:            
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root