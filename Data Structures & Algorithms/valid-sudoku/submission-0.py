from collections import defaultdict


def empty():
    return [defaultdict(bool) for _ in range(9)]

def square(row, col):
    def convert(i):
        if i in [0,1,2]:
            return 0
        if i in [3,4,5]:
            return 1
        if i in [6,7,8]:
            return 2
    top_left_r = convert(row)
    top_left_c = convert(col)
    return 3*top_left_r + top_left_c


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdicts = empty()
        coldicts = empty()
        squaredicts = empty()
        for rowI in range(len(board)):
            for colI, elem in enumerate(board[rowI]):
                if elem == ".":
                    continue
                squareI = square(rowI, colI)
                if rowdicts[rowI][elem] or coldicts[colI][elem] or squaredicts[squareI][elem]:
                    print(elem, rowdicts[rowI][elem], coldicts[colI][elem], squaredicts[squareI][elem])
                    return False
                rowdicts[rowI][elem] = True
                coldicts[colI][elem] = True
                squaredicts[squareI][elem] = True
        return True
            
