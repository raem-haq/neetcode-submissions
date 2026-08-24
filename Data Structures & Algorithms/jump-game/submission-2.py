class Solution:
    def canJump(self, nums: List[int]) -> bool:
        iHi = 0
        last = len(nums) - 1
        for i,n in enumerate(nums):
            if i <= iHi:
                iHi = max(iHi, i+n)
            else:
                return False
        return True