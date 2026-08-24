class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        elems = set(nums)
        max_len = 0
        for i in nums:
            if i in visited:
                continue
            m = i
            M = i
            l = 1
            chaining = True
            while chaining:
                chaining = False
                if M + 1 in elems:
                    visited.add(M+1)
                    l += 1
                    M += 1
                    chaining = True
                if m - 1 in elems:
                    visited.add(m-1)
                    l += 1
                    m -= 1
                    chaining = True
            if max_len < l:
                max_len = l
        return max_len