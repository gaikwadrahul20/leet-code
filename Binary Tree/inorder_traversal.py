class Solution:
    def inorderTraversal(self, root):
        stack = []
        in_order_list = []
        while root is not None or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root =  stack.pop()
                in_order_list.append(root.val)
                root = root.right
        return in_order_list