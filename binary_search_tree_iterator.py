# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: TreeNode):
        self.list = self.in_order(root)
        self.pointer = 0
        self.list_len = len(self.list)
    
    def next(self) -> int:
        self.pointer+=1
        return self.list[self.pointer-1]
        

    def hasNext(self) -> bool:
        if(self.pointer >= self.list_len):
            return False
        return True
    
    def in_order(self, root):
        path = []
        if root is None:
            return []
        path = path + self.in_order(root.left)
        path.append(root.val)
        path = path + self.in_order(root.right)
        return path
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()