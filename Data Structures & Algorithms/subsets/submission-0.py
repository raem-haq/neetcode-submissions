def add(arr):
    carry = 1
    for i in range(len(arr) - 1, - 1, - 1):
        if not carry:
            return arr
        if arr[i]:
            carry = 1
            arr[i] = 0
        else:
            carry = 0
            arr[i] = 1
    if carry:
        return []
    return arr

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bin_arr = [0]*(len(nums))
        subsets = []
        for _ in range(2**len(nums)):
            new_subset = []
            for b, x in zip(bin_arr, nums):
                if b == 1:
                    new_subset.append(x)
            subsets.append(new_subset)
            add(bin_arr)
        return subsets
            