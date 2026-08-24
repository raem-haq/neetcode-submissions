from collections import defaultdict
class TrieNode:
    def __init__(self, char=None, i=None, j=None):
        self.char = char
        self.children = defaultdict(list)
        self.pos = (i,j)
        self.reachable = False
        self.ends_word = False
    
    def __repr__(self):
        return (f"Char = {self.char}, Children = {self.children.keys()}, Pos = {self.pos}")

class SearchTrie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.ends_word = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        trie_board = [[TrieNode(board[i][j],i,j) for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                node = trie_board[i][j]
                if i - 1 >= 0:
                    n = trie_board[i-1][j]
                    node.children[n.char].append(n)
                if i + 1 < NUM_ROWS:
                    n = trie_board[i+1][j]
                    node.children[n.char].append(n)
                if j - 1 >= 0 :
                    n = trie_board[i][j-1]
                    node.children[n.char].append(n)
                if j + 1 < NUM_COLS:
                    n = trie_board[i][j+1]
                    node.children[n.char].append(n)
        
        root_trie = TrieNode()
        for row in trie_board:
            for trie_node in row:
                c = trie_node.char
                root_trie.children[c].append(trie_node)

        def dfs_trie(root, node, word="", visited=None, all_reachable=None):
            if not visited:
                visited = defaultdict(bool)
            if not all_reachable:
                all_reachable = set()
            

            if visited[node]:
                return all_reachable

            root.reachable = True
            if root.ends_word:
                all_reachable.add(word)

            
            visited[node] = True
            for c, child in root.children.items():
                for next_node in node.children[c]:
                    all_reachable.update(dfs_trie(child, next_node, word + c, visited, all_reachable))
            
            visited[node] = False
            return all_reachable


        search_trie = SearchTrie()
        for word in words:
            search_trie.addWord(word)
        
        return list(dfs_trie(search_trie.root, root_trie))