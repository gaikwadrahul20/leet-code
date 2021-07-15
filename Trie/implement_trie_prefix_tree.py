class TrieNode:
    def __init__(self, val='#'):
        self.val = None
        self.children = [None]*26
        self.is_end = False

'''Using array'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            child = current.children[ord(char) - 97]
            if child is None:
                child = TrieNode(char)
                current.children[ord(char) - 97] = child
            current = child
        current.is_end = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            child = current.children[ord(char) - 97]
            if child is None:
                return False
            current  = child
        return current.is_end        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            child = current.children[ord(char) - 97]
            if child is None:
                return False
            current  = child
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''Using Map'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            child = current.children.get(char)
            if child is None:
                child = TrieNode()
                current.children[char] = child
            current = child
        current.is_end = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            child = current.children.get(char)
            if child is None:
                return False
            current  = child
        return current.is_end    
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            child = current.children.get(char)
            if child is None:
                return False
            current  = child
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)