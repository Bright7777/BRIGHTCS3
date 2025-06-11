class TrieNode:
    def _init_(self):
        self.children = {}  # Dictionary to store children nodes
        self.is_end_of_word = False  # Flag to check end of a word

class Trie:
    def _init_(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return  node