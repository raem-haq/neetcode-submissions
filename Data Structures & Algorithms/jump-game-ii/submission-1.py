class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        min_hops = [float('inf')] * N
        min_hops[-1] = 0
        for i in range(N-2,-1,-1):
            if nums[i] > 0:
                min_hops[i] = min([min_hops[j] + 1 for j in range(i+1, min(len(nums), i+nums[i]+1))])
        return min_hops[0]