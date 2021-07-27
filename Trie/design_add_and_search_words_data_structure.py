class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            child = current.children.get(char)
            if child is None:
                child = TrieNode()
                current.children[char] = child
            current = child
        current.is_end = True

    def search(self, word: str, root=None) -> bool:
        if root is None:
            current = self.root
        else:
            current = root
        i = 0
        for char in word:
            if char == ".":
                for child in current.children:
                    if self.search(child + word[i+1:], current):
                        return True
                return False
            else:
                child = current.children.get(char)
                if child is None:
                    return False
            i+=1
            current = child
        
        return current.is_end
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

