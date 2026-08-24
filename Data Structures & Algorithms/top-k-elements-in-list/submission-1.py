class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        nums_by_freq = sorted([(i, nums_counter[i]) for i in nums_counter], key = lambda x:x[1], reverse=True)
        return [i[0] for i in nums_by_freq[0:k]]