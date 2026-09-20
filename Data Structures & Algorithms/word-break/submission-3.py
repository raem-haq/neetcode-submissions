class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            node = node.children.setdefault(char, TrieNode())

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, text: str):
        node = self.root

        for char in text:
            node = node.children.get(char)
            if node is None:
                return None

        return node

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #def sol(currTrieNode, trie, i, e):
        #    if i == len(s):
        #        return currTrieNode.is_end 
        #    #print(e, s[i])
        #    if currTrieNode.is_end:
        #        if sol(trie.root, trie, i, ""):
        #            return True
        #    currTrieNode = currTrieNode.children.get(s[i], None)
        #    if currTrieNode is None:
        #        return False
        #    e+= s[i]
        #    return sol(currTrieNode, trie, i+1, e)
#
        #trie = Trie()
        #for w in wordDict:
        #    trie.insert(w)
        #return sol(trie.root, trie, 0, e="")
#
        wordSet = set(wordDict)
        trueAt = []
        for end in range(len(s)):
            if s[:end+1] in wordSet:
                trueAt.append(end)
            else:
                for start in trueAt:
                    if s[start+1:end+1] in wordSet:
                        trueAt.append(end)
                        break
        return len(s) - 1 in trueAt




#words(x|c:s) = is_word(xc) and words(s) | words(xc|s)  




