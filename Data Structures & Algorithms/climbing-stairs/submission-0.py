class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        fib = 1
        fib2 = 0
        while i < n:
            i += 1
            t = fib2
            fib2 = fib
            fib = fib + t
        return fib
            