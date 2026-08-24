class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif prices[i] > low:
                maxP = max(maxP, prices[i] - low)
        return maxP
