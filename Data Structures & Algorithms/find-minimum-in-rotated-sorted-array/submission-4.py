class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[-1] > nums[0]:
            return nums[0]
        hi = n - 1
        lo = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            v = nums[mid]
            if mid > 0 and nums[mid-1] > v:
                return v
            elif v > nums[-1]:
                lo = mid + 1
            else:
                hi = mid - 1

# https://chatgpt.com/s/t_68a873d387bc8191a2a704adb3c9a0ca
"""
GPT SOL:

lo, hi = 0, n-1
while lo < hi: // lo cannot exceed hi
    mid = (lo + hi) // 2
    if nums[mid] > nums[hi]: // hi is always on the rightside increasing subsection 
        lo = mid + 1 // mid < hi, mid +1 <= hi, lo <= hi
    else:
        hi = mid // hi_new = (lo+hi_prev) //2 > (lo+lo) //2 = lo
return nums[lo] // when loop terminates hi == lo


"""
            