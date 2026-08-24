class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo, hi = 0 , len(heights) - 1
        max_area = 0
        while lo < hi:
            ll, hh = heights[lo], heights[hi]
            area = min(ll, hh)*(hi-lo)
            max_area = max(max_area, area)
            if ll < hh:
                lo += 1
            else:
                hi -= 1
        return max_area