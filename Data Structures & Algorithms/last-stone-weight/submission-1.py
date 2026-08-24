from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-s for s in stones]
        heapify(hp)
        while len(hp) > 1:
            y = -heappop(hp)
            x = -heappop(hp)
            if x < y:
                heappush(hp, x-y)
        return 0 if not hp else -hp[0]
