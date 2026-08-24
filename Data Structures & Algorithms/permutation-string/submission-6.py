from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        d2 = Counter(s2)
        lo = 0
        hi = len(s2) - 1
        while lo <= hi:
            if d1 == d2:
                return True
            l, r = s2[lo], s2[hi]
            if d1[l] > d2[l] or d1[r] > d2[r]:
                return False
            if d1[l] == d2[l] and d1[r] == d2[r]:
                return False
            if d1[l] < d2[l]:
                lo += 1
                d2[l] -= 1
            if d1[r] < d2[r]:
                hi -= 1
                d2[r] -= 1
        return False 