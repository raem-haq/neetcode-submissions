class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        maxL = 0
        for i, c in enumerate(s):
            if (c in seen and seen[c] >= start):
                maxL = max(maxL, i - start)
                start = seen[c] + 1
            elif i == len(s) - 1:
                maxL = max(maxL, i - start + 1)
            seen[c] = i
        return maxL