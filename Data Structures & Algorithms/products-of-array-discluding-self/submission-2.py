class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #numZeros = 0
        #prod = 1
        #for i in nums:
        #    if i == 0:
        #        numZeros += 1
        #    else:
        #        prod *= i
        #ans = []
        #for i in nums:
        #    if i == 0 and numZeros == 1:
        #        ans.append(prod)
        #    elif numZeros >= 1:
        #        ans.append(0)
        #    else:
        #        ans.append(prod//i)
        #return ans
        prefixProds = []
        prod = 1
        for i in nums:
            prod *= i
            prefixProds.append(prod)
        
        suffixProds = [0]*len(nums)
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            prod *= nums[i]
            suffixProds[i] = prod
        print(prefixProds, suffixProds)

        ans = [0]*len(nums)
        for i in range(len(nums)):
            if i == len(nums) - 1:
                ans[i] = prefixProds[-2]
            elif i == 0:
                ans[i] = suffixProds[1] 
            else:        
                ans[i] = prefixProds[i-1] * suffixProds[i+1]
        return ans