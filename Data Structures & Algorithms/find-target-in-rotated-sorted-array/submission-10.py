"""
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
"""
#Struggled to join unrotated and rotated cases
#using lo-hi as endpoints was an idea i considered
#based on the gpt sol to the previous question
#but I struggled to find an algo

#GPT:
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1
"""
# AFTER WATCHING VIDEO
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            # shockingly theres a big difference between n > nums[hi]
            # and nums[lo] <= n
            # you just need to be consistent with which ever you use
            if nums[mid] > nums[hi]: # in the left half
                #can condense dradt-1 conditional  
                if nums[lo] > target or nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else: # in the right half
                #(condensed:)
                #dont think "want left half", think "want to go left"
                if target > nums[hi] or nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1
