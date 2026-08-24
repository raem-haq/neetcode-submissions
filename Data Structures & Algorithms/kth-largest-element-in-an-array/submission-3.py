#USE median-of-three quickselect FOR O(1) SPACE

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #MIN HEAP
        #hp = []
        #for n in nums:
        #    heapq.heappush(hp, n)
        #    if len(hp) > k:
        #        heapq.heappop(hp)
        #return hp[0]

        #QUICK SELECT
        while True:
            pivot = nums.pop()
            lower = [n  for n in nums if n < pivot]
            higher = [n for n in nums if n >= pivot]
            pos = len(higher)+1
            if k == pos:
                return pivot
            if k > pos:
                k -= pos
                nums = lower
            else:
                nums = higher