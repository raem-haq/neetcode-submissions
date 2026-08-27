decodings = [str(i) for i in range(1, 27)]

class Solution:
    def numDecodings(self, s: str) -> int:
        def res(s, i, memo={}):
            if i >= len(s):
                return 1
            if i in memo:
                return memo[i]
            t = 0
            for end in range(i, len(s)):
                if s[i: end+1] in decodings:
                    t += res(s, end+1)
            memo[i] = t
            return t
        return res(s, 0)