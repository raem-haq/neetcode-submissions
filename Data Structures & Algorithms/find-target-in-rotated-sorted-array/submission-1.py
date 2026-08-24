class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        if nums[0] <= nums[-1]:
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
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > nums[-1]: # in the left half
                    if nums[lo] <= target: # want left half
                        if nums[mid] < target:
                            lo = mid + 1
                        else:
                            hi = mid - 1
                    else: # want right half
                        lo = mid + 1                        
                else: # in the right half
                    if nums[0] <= target: # want left half
                        hi = mid - 1
                    else: # want right half
                        if nums[mid] < target:
                            lo = mid + 1
                        else:
                            hi = mid - 1
        return -1