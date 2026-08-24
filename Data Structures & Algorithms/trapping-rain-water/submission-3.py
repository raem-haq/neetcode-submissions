class Solution:
    def trap(self, height: List[int]) -> int:
        big = 0
        passed_from = 0
        hs = 0
        water = 0
        for h in height:
            #print(h, big, passed_from, hs, water)
            if big <= h:
                water += big * passed_from
                water -= hs
                big = h
                hs = passed_from = 0
            else:
                hs += h
                passed_from += 1
        big = 0
        passed_from = hs = 0
        for h in height[::-1]:
            if big < h: # < here to avoid double-counting
                water += big * passed_from
                water -= hs
                big = h
                hs = passed_from = 0
            else:
                hs += h
                passed_from += 1
        return water
        
                


