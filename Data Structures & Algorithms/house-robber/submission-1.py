class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(i, memo={}):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            #if i == len(nums) - 1:
            #    return nums[-1]
            #if i == len(nums) - 2:
            #    return nums[-2]
            
            ans = nums[i] + max(recurse(i + 2, memo), recurse(i + 3, memo))
            memo[i] = ans
            return ans
        if len(nums) == 1:
            return nums[0]
        else:
            return max(recurse(0), recurse(1))
