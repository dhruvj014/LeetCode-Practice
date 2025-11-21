class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
    
    def containschar(self,ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self,ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self,ch):
        return self.links[ord(ch) - ord('a')]
    
    def setEnd(self):
        self.flag = True

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not node.containschar(word[i]):
                node.put(word[i],Node())
            node = node.get(word[i])
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        i = 0
        while i < len(word):
            ch = word[i]
            if node.containschar(ch):
                node = node.get(ch)
                i += 1    
                if i == len(word):
                    return node.flag
            else:
                break
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        i = 0
        while i < len(prefix):
            ch = prefix[i]
            if node.containschar(ch):
                node = node.get(ch)
                i += 1
                if i == len(prefix):
                    return node != None
            else:
                break
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)