class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            n = nums[mid]
            if n == target:
                return mid
            elif n < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1