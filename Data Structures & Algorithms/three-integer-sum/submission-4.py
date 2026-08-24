from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            low, high = i + 1, n - 1

            while low < high:
                two_sum = nums[low] + nums[high]
                if two_sum == target:
                    trips.append([nums[i], nums[low], nums[high]])
                    #do two-pointer on sublist of [low+1, high-1]
                    low += 1
                    high -= 1
                    # Skip duplicates for the second and third numbers
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif two_sum < target:
                    low += 1
                else:
                    high -= 1

        return trips
