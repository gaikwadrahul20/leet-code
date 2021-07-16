class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            child = current.children.get(char)
            if child is None:
                child = TrieNode()
                current.children[char] = child
            current = child
        current.is_end = True
    
    def search_word(self, word):
        current = self.root
        i = 1
        for char in word:
            child = current.children.get(char)
            if child is not None and child.is_end:
                return word[:i]
            elif child is None:
                return False
            current = child
            i+=1
        return False
        
class Solution: 
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = Trie()
        result = []
        for word in dictionary:
            tree.insert(word)
        
        words = sentence.split()
        for word in words:
            r_word = tree.search_word(word)
            if(r_word):
                result.append(r_word)
            else:
                result.append(word)
        
        return " ".join(result)
