from collections import defaultdict


def empty():
    return [set() for _ in range(9)]

def square(row, col):
    return 3*(row//3) + (col//3)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsets = empty()
        coldsets = empty()
        squaresets = empty()
        for rowI in range(len(board)):
            for colI, elem in enumerate(board[rowI]):
                if elem == ".":
                    continue
                squareI = square(rowI, colI)
                if (
                    elem in rowsets[rowI] or
                    elem in coldsets[colI] or
                    elem in squaresets[squareI]
                ):
                    return False
                rowsets[rowI].add(elem)
                coldsets[colI].add(elem)
                squaresets[squareI].add(elem)
        return True
            
