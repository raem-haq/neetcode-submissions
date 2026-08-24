def alpha(c):
    return ((c >= 'a') and (c <= 'z')) or (c >= '0' and c <= '9')
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        high = len(s) -1
        low = 0
        while low <= high:
            ls = s[low]
            hs = s[high]

            skip = False
            if not alpha(ls):
                low += 1
                skip = True
            if not alpha(hs):
                high -= 1
                skip = True
            if skip:
                continue

            if ls != hs:
                return False
            low +=1
            high -= 1
        return True