# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Below solution is giving time limit: just for 1 case
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized_object = self.traverse_tree(root)
        serialized_object = "_".join(serialized_object)
        
        return serialized_object

    def traverse_tree(self, root):
        if root == None:
            return ["None"]
        
        queue = collections.deque()
        queue.append(root)
        tree_list = []
        while queue:
            current = queue.popleft()
            if current:
                queue.append(current.left)
                queue.append(current.right)
                tree_list.append(str(current.val))
            else:
                tree_list.append("None")
        return tree_list
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split("_")
        tree_nodes = []
        for val in tree:
            if val != "None":
                node = TreeNode()
                node.val = val
                node.left = None
                node.right = None
                tree_nodes.append(node)
            else:
                tree_nodes.append(None)
        
        result = tree_nodes[0]
        prev = collections.deque()
        prev.append(tree_nodes[0])
        i = 1
        while i in range(len(tree_nodes)):
            prev_len = len(prev)
            j = 0
            while j in range(prev_len) and i<len(tree_nodes):
                node = prev.popleft()
                if node is not None:
                    node.left = tree_nodes[i]
                    prev.append(node.left)
                    node.right = tree_nodes[i+1]
                    prev.append(node.right)
                    i+=2
                else:
                    prev.append(None)
                    prev.append(None)
                j+=1
        return result 
                
                
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# Copied solution
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()