#FROM VIDEO
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        numStartI = 0
        decoded = []
        while numStartI < len(s):
            htagI = numStartI + 1
            while s[htagI] != '#':
                htagI += 1
            length = int(s[numStartI:htagI])
            strStartI = htagI + 1
            strEndI = strStartI + length
            decoded.append(s[strStartI:strEndI])
            numStartI = strEndI
        return decoded