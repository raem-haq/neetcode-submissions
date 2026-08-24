import heapq

class KthLargest:



    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        for n in nums:
            heapq.heappush(self.hp, -n)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, -val)
        #print(self.hp)
        tmp = []
        for _ in range(self.k):
            tmp.append(heapq.heappop(self.hp))
        kth = -1*tmp[-1]
        for t in tmp:
            heapq.heappush(self.hp, t)
        return kth