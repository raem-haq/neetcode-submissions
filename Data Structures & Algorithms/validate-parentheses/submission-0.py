class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        open_p = {'(', '{', '['}
        pairs = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in open_p:
                stck.append(c)
            else:
                if not stck:
                    return False
                b = stck.pop()
                if c != pairs[b]:
                    return False
        return not stck