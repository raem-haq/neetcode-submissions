class Solution:
    def canJump(self, nums: List[int]) -> bool:
        iHi = 0
        for i,n in enumerate(nums):
            if i <= iHi:
                iHi = max(iHi, i+n)
            else:
                return False
        return True