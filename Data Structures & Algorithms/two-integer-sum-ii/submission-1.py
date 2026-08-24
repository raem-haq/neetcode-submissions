class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low <= high: # always a sol
            calc = numbers[low] + numbers[high]
            if calc == target:
                return [low + 1, high + 1]
            elif calc < target:
                low += 1
            else:
                high -= 1
         