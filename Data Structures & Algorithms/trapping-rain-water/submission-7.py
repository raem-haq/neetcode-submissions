
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        width = interior_heights = 0
        water = 0

        for h in height:
            if left_max <= h:
                water += left_max * width - interior_heights
                left_max = h
                width = interior_heights = 0
            else:
                interior_heights += h
                width += 1
        
        right_max = width = interior_heights = 0
        for h in height[::-1]:
            if right_max < h: # < here to avoid double-counting
                water += right_max * width - interior_heights
                right_max = h
                width = interior_heights = 0
            else:
                interior_heights += h
                width += 1
        return water
        
                


