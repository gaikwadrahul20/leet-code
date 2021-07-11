# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Simple two traversal solution: Refer GFG (https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.path_to_node(root, p)
        q_path = self.path_to_node(root, q)
        
        i = 0
        p_len = len(p_path)
        q_len = len(q_path)
        while (i< q_len and i< p_len):
            if  p_path[i].val != q_path[i].val:
                break
            i+=1
            
        return p_path[i-1]
        
    def path_to_node(self, tree, node):
        if tree is None:
            return None
        path = []
        path.append(tree)
        if (tree.val == node.val):
            return path
        
        left_path = self.path_to_node(tree.left, node)
        right_path = self.path_to_node(tree.right, node)
        if (left_path is not None):
            path.extend(left_path)
            return path
        elif(right_path is not None):
            path.extend(right_path)
            return path
        else:
            path.pop()
            return None
        
# Single traversal solution: Refer GFG (https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
				# If looking for me, return myself
        if root == p or root == q:
            return root
        
        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way, 
        # because in such scenarios, node where 'p' found is LCA
            return left or right

# Iterative see later