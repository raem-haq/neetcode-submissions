class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solves = []
        nums.sort()
        stack = [([], 0)]
        for n in nums:
            new_stack = []
            while stack:
                arr, total = stack.pop()
                temp = []
                while total <= target:
                    if total == target:
                        solves.append(arr+temp)
                        break
                    new_stack.append((arr+temp, total))   
                    temp.append(n)
                    total += n
            stack = new_stack
        return solves