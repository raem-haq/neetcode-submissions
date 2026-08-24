from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        elem_i = {x : i for i, x in enumerate(nums)} # stores last index for duplicates
        
        
        triplets = []
        seen = set()
        for i, x in enumerate(nums):
            for j in range(i+1, len(nums)):
                y = nums[j]
                want = - x - y
                if want in elem_i:
                    xs = [elem_i[x], elem_i[y], elem_i[want]]
                    xs.sort()
                    sol = tuple(xs)
                    k = elem_i[want]
                    if k > j and not sol in seen:
                        seen.add(sol)
                        triplets.append([x, y, want])
        print(seen)
        return triplets


"""
elem_i_2 = defaultdict(list)
        for i, x in enumerate(nums):
            elem_i_2[x].append(i)
"""