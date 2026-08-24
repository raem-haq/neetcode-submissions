class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum = [0 for _ in range(len(nums) + 1)]
        for i, v in enumerate(nums):
            presum[i] = presum[i-1] + nums[i]
        print(presum)
        l = []
        for i, v in enumerate(presum):
            if i == len(presum) - 1:
                continue
            if presum[i-1] == presum[-2] - presum[i]:
                return i
        return -1