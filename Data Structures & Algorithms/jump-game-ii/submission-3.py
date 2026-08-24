class Solution:
    def jump(self, nums: List[int]) -> int:
        iHi = 0
        iLo = 0
        hops = 0
        while iHi < len(nums) - 1:
            iHi_old = iHi
            for i in range(iLo, iHi_old+1):
                iHi = max(iHi, i+nums[i])
            iLo = iHi_old + 1
            hops += 1
        return hops