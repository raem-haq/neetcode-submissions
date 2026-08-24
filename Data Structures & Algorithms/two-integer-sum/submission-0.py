class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements_indices = {}
        for i, e in enumerate(nums):
            if e in elements_indices:
                elements_indices[e].append(i)
            else:
                elements_indices[e] = [i]
        for i, e in enumerate(nums):
            pair = target - e
            if pair in elements_indices:
                for j in elements_indices[pair]:
                    if j != i:
                        return [i,j]
        return -1 
            