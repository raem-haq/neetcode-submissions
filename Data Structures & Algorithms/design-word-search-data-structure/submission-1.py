class LetterNode:
    def __init__(self):
        self.next_words = {}
        self.ends_word = False

class WordDictionary:

    def __init__(self):
        self.root = LetterNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.next_words:
                node.next_words[c] = LetterNode()
            node = node.next_words[c]
        node.ends_word = True


    def search(self, word: str) -> bool:
        queue = [ (0, self.root)]
        while queue:
            i, node = queue.pop()
            if i >= len(word):
                if node.ends_word:
                    return True
            else:
                char = word[i]
                if char == ".":
                    for next_node in node.next_words.values():
                        queue.append((i+1, next_node))
                elif char in node.next_words:
                    queue.append( (i+1, node.next_words[char]) )
        return False