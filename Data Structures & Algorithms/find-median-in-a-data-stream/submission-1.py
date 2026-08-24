import heapq
class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if self.high and num > self.high[0]:
            heapq.heappush(self.high, num)
        else:
            heapq.heappush_max(self.low, num)

        if len(self.high) > len(self.low):
            heapq.heappush_max(self.low, heapq.heappop(self.high))
        elif len(self.low) > 1 + len(self.high):
            heapq.heappush(self.high, heapq.heappop_max(self.low))
        print(self.low, self.high)



    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (self.low[0] + self.high[0])/2
        else:
            return self.low[0]