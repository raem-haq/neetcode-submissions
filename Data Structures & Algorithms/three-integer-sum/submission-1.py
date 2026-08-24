class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        elem_i = {x : i for i, x in enumerate(nums)} # stores last index for duplicates
        triplets = []
        seen = set()
        for i, x in enumerate(nums):
            for j in range(i+1, len(nums)):
                y = nums[j]
                want = - x - y
                xs = [x,y,want]
                xs.sort()
                my_hash = (2**xs[0]) * (3**xs[1]) * (5 ** xs[2])
                if want in elem_i and my_hash not in seen:
                    k = elem_i[want]
                    if k > i and k > j:
                        seen.add(my_hash)
                        print(i, j, k, want)
                        triplets.append([x, y, want])
        return triplets
