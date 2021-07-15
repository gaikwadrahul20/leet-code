# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''Iterative: worst/Best solution and too complicated'''
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        result = root
        prev = None
        pointer = None
        while root is not None:
            if root.val == key:
                if (root.left and root.right):
                    succ = root.right
                    succ_parent = None
                    while(succ.left):
                        succ_parent = succ
                        succ = succ.left

                    tmp = root.val
                    root.val = succ.val
                    succ.val = tmp
                    
                    if succ_parent:
                        succ_parent.left = succ.right
                    else:
                        root.right = succ.right
                        
                
                elif(root.right):
                    if(prev is None):
                        root = root.right
                        return root
                    else:
                        if(pointer == "left"):
                            prev.left = root.right
                        else:
                            prev.right = root.right
                elif(root.left):
                    if(prev is None):
                        root = root.left
                        return root
                    else:
                        if(pointer == "left"):
                            prev.left = root.left
                        else:
                            prev.right = root.left

                else:
                    if prev and pointer == "right":
                        prev.right = None
                    elif prev and pointer == "left":
                        prev.left = None
                    else:
                        return None
                break
        
            elif(root.left and key < root.val):
                prev = root
                pointer = "left"
                root = root.left
                
            elif(root.right and key > root.val):
                prev = root
                pointer = "right"
                root = root.right
            else:
                break
            
        return result




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''Iterative'''
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
            
            
        elif(root.left and key < root.val):
            root.left = self.deleteNode(root.left, key)
        elif(root.right and key > root.val):
            root.right = self.deleteNode(root.right, key)

        return root