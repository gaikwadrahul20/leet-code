inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(enumerate(inorder))
print(inorder[-1])
print(inorder[1:-1])


for index, val in enumerate(inorder):
    print(index, val)
    
# ans = [3,9,20,null,null,15,7]

# Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        root = TreeNode()
        root.val = postorder.pop()
        
        for index in range(len(inorder)):
            if root.val == inorder[index]:
                break
        
        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:])
        return root
        
        
        
# Iterative yet to solve