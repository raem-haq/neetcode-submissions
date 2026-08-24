class Solution:
    def maxArea(self, heights: List[int]) -> int:
        compressed = list(enumerate(heights))
        compressed.sort(reverse=True, key=lambda x: x[1])
        i, _ = compressed[0]
        j, h = compressed[1]
        k, K = min(i,j) , max(i,j)
        volume = h * (K - k)
        for i, x in compressed[2:]:
            if i > k and i < K:
                continue
            k, K = min(i,k) , max(i,K)
            v = x * (K - k)
            if v > volume:
                volume = v
        return volume
        
