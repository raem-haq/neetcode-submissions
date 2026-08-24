class PrefixTree:

    def __init__(self):
        self.transitions = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        if word == "":
            self.is_word = True
            return
        first_char = word[0]

        if first_char in self.transitions:
            next_trie = self.transitions[first_char]
            next_trie.insert(word[1:])
        else:
            new_trie = PrefixTree()
            new_trie.insert(word[1:])
            self.transitions[first_char] = new_trie
        

    def search(self, word: str) -> bool:
        trie = self
        for c in word:
            if c in trie.transitions:
                trie = trie.transitions[c]
            else:
                return False
        return trie.is_word

    def startsWith(self, prefix: str) -> bool:
        trie = self
        for c in prefix:
            if c in trie.transitions:
                trie = trie.transitions[c]
            else:
                return False
        return True
        