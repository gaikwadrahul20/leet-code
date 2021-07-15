"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = collections.deque()
        if root is None:
            return root
        if root.left is None:
            return root
        queue.append(root.left)
        queue.append(root.right)
        while (queue):
            q_len = len(queue)
            for i in range(q_len-1):
                current = queue.popleft()
                current.next = queue[0]
                if current.right is not None:
                    queue.append(current.left)
                    queue.append(current.right)
            last = queue.popleft()
            if last.left is not None:
                queue.append(last.left)
                queue.append(last.right)
        return root

                
                
        
        