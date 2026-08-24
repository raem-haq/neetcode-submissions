
class Point:
    def __init__(self, s):
        self.s = s

    def __lt__(self, P):
        s = self.s
        t = P.s
        if s[0] == t[0]:
            return s[1] < t[1]
        if s[1] == t[1]:
            return s[0] < t[0]
        return self.norm2(s) < self.norm2(t)

    def norm2(self, s):
        return (s[0]**2 + s[1]**2)
    

import heapq
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pObj = [Point(s) for s in points]
        ret = []
        for p in pObj:
            heapq.heappush_max(ret, p)
            if len(ret) > k:
                heapq.heappop_max(ret)
        return [p.s for p in ret]
