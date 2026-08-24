class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subsets = []

        # loop from 0 to 2^n - 1
        for mask in range(1 << n):  # 1 << n is 2^n
            subset = []
            for i in range(n):
                # check if the i-th bit is set
                if mask & (1 << i):
                    subset.append(nums[i])
            subsets.append(subset)

        return subsets
