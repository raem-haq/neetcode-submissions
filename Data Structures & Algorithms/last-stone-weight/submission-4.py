#BUCKET SORT APPROACH IS O(n+max) -- see sol

from heapq import heapify_max, heappop_max, heappush_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = stones
        heapify_max(hp)
        while len(hp) > 1:
            y = heappop_max(hp)
            x = heappop_max(hp)
            if x < y:
                heappush_max(hp, y-x)
        return 0 if not hp else hp[0]
