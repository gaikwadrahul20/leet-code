class TrieNode:
    def __init__(self,val=0):
        self.val = val
        self.children = {}
        self.is_end = False

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        

    def insert(self, key: str, val: int) -> None:
        current = self.root
        # childs = []
        for char in key:
            child = current.children.get(char)
            if child is None:
                child = TrieNode(val)
                current.children[char] = child
            current = child
        current.val = val
        current.is_end = True
        

    def sum(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            child = current.children.get(char)
            if child is None:
                return 0
            current = child
        result = 0
        queue = collections.deque()
        queue.append(current)
        while queue:
            current = queue.popleft()
            if current.is_end:
                result += current.val
            for child in current.children:
                queue.append(current.children[child])
        return result
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)