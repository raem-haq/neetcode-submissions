class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        val = nums[-1]
        val_neg = nums[-1]
        ans = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            old_val = val
            val = max(nums[i], nums[i]*val_neg, nums[i]*val)
            val_neg = min(nums[i], nums[i]*val_neg, nums[i]*old_val)
            ans = max(ans, val)
        return ans