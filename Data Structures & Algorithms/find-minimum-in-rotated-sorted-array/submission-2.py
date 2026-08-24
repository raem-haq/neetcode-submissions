class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        hi = n - 1
        lo = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            v = nums[mid]
            if (mid == n - 1 and nums[mid] < nums[mid-1] or
                nums[mid-1] >= v and v <= nums[mid + 1]
            ):
                return v
            elif v > nums[-1]:
                lo = mid + 1
            else:
                hi = mid - 1
                
            