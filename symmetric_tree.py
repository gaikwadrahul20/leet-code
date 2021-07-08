# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.are_two_tree_mirror(root.left, root.right)
    
    def are_two_tree_mirror(self, tree_1, tree_2):
        if tree_1 is None and tree_2 is None:
            return True
        if tree_1 is None and tree_2 is not None:
            return False
        if tree_1 is not None and tree_2 is None:
            return False
        if tree_1.val != tree_2.val:
            return False
        if (self.are_two_tree_mirror(tree_1.left, tree_2.right) and self.are_two_tree_mirror(tree_1.right, tree_2.left)):
            return True

# Iterative