def hours_taken(piles: List[Int], k : int)  -> int:
    h = 0
    for p in piles:
        h += (p // k) + (p % k > 0)
    return h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = (int(max(piles) / h) + 1) * len(piles)
        lo = 1
        while lo < hi:
            mid = (lo + hi)//2
            if hours_taken(piles, mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo