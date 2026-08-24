class Solution:
    def jump(self, nums: List[int]) -> int:
        iHi = 0
        hops = 0
        while iHi < len(nums) - 1:
            for i in range(iHi+1):
                iHi = max(iHi, i+nums[i])
            hops += 1
        return hops