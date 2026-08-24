class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if n < 0:
                n += len(nums)
            if nums[n] < 0:
                return n
            nums[n] -= len(nums)