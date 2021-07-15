# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Height:
#     def __init__(self):
#         self.height = 0

# class Solution:
#     def isBalanced(self, root: TreeNode, height = Height()) -> bool:
#         if root is None:
#             height.height = 0
#             return True
        
#         left_height = Height()
#         right_height = Height()
        
#         lh = self.isBalanced(root.left, left_height)
#         rh = self.isBalanced(root.right, right_height)
        
#         height.height = max(left_height.height, right_height.height) + 1
        
#         if (abs(left_height.height-right_height.height)<= 1):
#             return lh and rh
        
#         return False

str = "Testing"
for val in str:
    print(val)