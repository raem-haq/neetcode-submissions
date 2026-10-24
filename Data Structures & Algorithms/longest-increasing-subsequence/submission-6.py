from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            j = bisect_left(tails, x)  
            if j == len(tails):
                tails.append(x)
            else:
                tails[j] = x
        return len(tails)