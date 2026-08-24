import heapq
from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp = []
        for n in nums[:k]:
            heapq.heappush(hp, -n)
        maxes = [-hp[0]]
        banned = defaultdict(int)
        for i in range(k, len(nums)):
            banned[nums[i-k]] += 1
            heapq.heappush(hp, -nums[i])
            M = -heapq.heappop(hp)
            while hp and banned[M] > 0:
                banned[M] -= 1
                M = -heapq.heappop(hp)
            maxes.append(M)
            heapq.heappush(hp, -M)
        return maxes