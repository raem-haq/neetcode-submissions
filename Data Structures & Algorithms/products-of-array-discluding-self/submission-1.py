class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        prod = 1
        for i in nums:
            if i == 0:
                numZeros += 1
            else:
                prod *= i
        ans = []
        for i in nums:
            if i == 0 and numZeros == 1:
                ans.append(prod)
            elif numZeros >= 1:
                ans.append(0)
            else:
                ans.append(prod//i)
        return ans
