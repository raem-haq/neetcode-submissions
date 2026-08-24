class Solution:
    def trap(self, height: List[int]) -> int:
        indexed = sorted(enumerate(height), key=lambda x: -x[1])

        lo = hi = indexed[0][0]
        water = 0

        for i, h in indexed[1:]:
            if lo < i < hi:
                water -= h
            elif i < lo:
                water += h * (lo - i - 1)
                lo = i
            elif i > hi:
                water += h * (i- hi - 1)
                hi = i
        
        return water

