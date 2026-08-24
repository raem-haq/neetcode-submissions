from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ds = Counter(s)
        dt = Counter(t)

        for c in dt.keys():
            if dt[c] > ds[c]:
                return ""

        def rec(i : int, j: int, d: Dict[str, int]) -> (int, int, int):
            #preprocessing
            #remove unnecessary characters from window (ones not in t)
            while dt[s[i]] == 0:
                d[s[i]] -= 1
                i += 1
            while dt[s[j]] == 0:
                d[s[j]] -= 1
                j -= 1
            
            #check for invalid cases
            if i > j:
                return (j, j-1, float('inf'))

            # if the window has all the characters of t (inc duplicates) and no more
            # you can't shrink further
            #if dt[s[i]] == ds[s[i]] and dt[s[j]] == ds[s[j]]:
            #    return (i, j, j-i+1)

            x, y, l = i, j, j-i+1
            
            #shorten from left if possible
            if dt[s[i]] < d[s[i]]:
                d[s[i]] -= 1
                x1, y1, l1 = rec(i+1, j, d)
                d[s[i]] += 1
                if l1 < l:
                    x, y, l = x1, y1, l1

            #shorten from right if possible
            if dt[s[j]] < d[s[j]]:
                d[s[j]] -= 1
                x2, y2, l2 = rec(i, j-1, d)
                d[s[j]] += 1
                if l2 < l:
                    x, y, l = x2, y2, l2
            
            return (x, y, l)
            
        x, y, _ = rec(0, len(s) - 1, ds)
        return s[x:y+1]