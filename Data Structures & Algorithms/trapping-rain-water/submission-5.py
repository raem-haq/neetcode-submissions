class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while i < j:
            if height[i] < height[j]:
                # Left side is lower, so it determines water level here
                if height[i] >= left_max:
                    left_max = height[i]
                else:
                    water += left_max - height[i]
                i += 1
            else:
                # Right side is lower (or equal), so it determines water level here
                if height[j] >= right_max:
                    right_max = height[j]
                else:
                    water += right_max - height[j]
                j -= 1

        return water

        
                


