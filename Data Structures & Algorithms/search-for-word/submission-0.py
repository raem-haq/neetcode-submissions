class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(word, i, rowI, colI):
            if i == len(word):
                return True
            if not (rowI >= 0 and rowI < len(board) and colI >= 0 and colI < len(board[0]) and board[rowI][colI] == word[i]):
                return False
            
            board[rowI][colI] = "*"
            ret = (dfs(word, i+1, rowI + 1, colI) or
                dfs(word, i+1, rowI - 1, colI) or
                dfs(word, i+1, rowI, colI + 1) or
                dfs(word, i+1, rowI, colI - 1))
            board[rowI][colI] = word[i]
            return ret
        
        for rowI in range(len(board)):
            for colI in range(len(board[0])):
                if dfs(word, 0, rowI, colI):
                    return True
        return False