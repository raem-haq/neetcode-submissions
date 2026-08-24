class Solution:
    def maxArea(self, heights: List[int]) -> int:
        indexed = sorted(enumerate(heights), key=lambda x: -x[1])

        lo = hi = indexed[0][0]
        max_area = 0

        for i, h in indexed[1:]:
            if lo < i < hi:
                continue
            lo, hi = min(lo, i), max(hi, i)
            max_area = max(max_area, h * (hi - lo))
        
        return max_area
